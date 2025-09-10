# Quiz_Class.py

import re, time
from IPython.display import display, HTML, clear_output
import ipywidgets as widgets
from threading import Timer

class AutoResizingInput:
  def __init__(self):
    self.input_box = widgets.Text(
      placeholder='Απάντηση...',
      layout=widgets.Layout(width='95px', min_width='95px')
    )
    self.input_box.observe(self._update_width, names='value')

  def _update_width(self, change):
    char_count = len(change['new'])
    new_width = max(95, min(800, char_count * 8))
    self.input_box.layout.width = f'{new_width}px'

  def get_widget(self):
    return self.input_box

class Quiz:
  def __init__(self, questions):
    self.questions = questions
    self.index = 0
    self.score = 0
    self.total = len(questions)
    self.selected_answer = None
    self.option_buttons = []
    self.output = widgets.Output()

    # Buttons
    self.prev_btn   = widgets.Button(description='Προηγούμενη', button_style='')
    self.submit_btn = widgets.Button(description='Υποβολή', button_style='info')
    self.retry_btn  = widgets.Button(description='Επανάληψη', button_style='warning')
    self.next_btn   = widgets.Button(description='Επόμενη',   button_style='primary')

    # Event bindings
    self.prev_btn.on_click(self.prev_question)
    self.submit_btn.on_click(self.submit_answer)
    self.retry_btn.on_click(self.retry_question)
    self.next_btn.on_click(self.next_or_finish)

    # State
    self.current_answer_widgets = []
    self.feedback_label = widgets.HTML("")
    self.message_label  = widgets.HTML("")
    self.answered_this_question = False
    self.scored_indices = set()

    self.display_quiz()

  @property
  def display(self):
    display(self.output)

  def _inject_code_css(self):
    return HTML('''
    <style>
    .quiz-container code {
      background-color: #f4f4f4;
      color: #c7254e;
      padding: 4px 6px;
      border-radius: 4px;
      font-family: monospace;
    }
    </style>
    ''')

  def _inject_round_button_css(self):
    display(HTML('''
    <style>
    .round-button {
      position: relative;
      top: 4px;
      border-radius: 50% !important;
      background-color: #f0f0f0f0;
      color: white;
      width: 20px;
      height: 20px;
      font-size: 10px;
      text-align: center;
      line-height: 1;
      vertical-align: middle;
      padding: 0;
      box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
      border: 1px solid #ccc;
    }
    .round-button:hover {
      background-color: #D3D3D3; /* Darker gray on hover */
    }
    </style>
    '''))

  def _inject_codebox_css(self):
    display(HTML("""
    <style>
    .py-code {
      background-color: #ffe;
      border: 1px solid #ccc;
      padding: 4px;
      border-radius: 4px;
      white-space: pre;
      tab-size: 4;
      font-family: monospace;
    }
    </style>
    """))


  # --- Buld the multiple choice question type (MCS) so that the buttons render html tags ---
  def show_mathjax_question(self, question_text, label_pairs):
    # Render the question
    display(HTML(f"""
    <div class='quiz-container'>{question_text}</div>
    <script>
      if (window.MathJax) {{
      MathJax.typesetPromise();
      }}
    </script>
    """))
    # Display each row one by one

    # Create a unique class name for each button
    for i, (btn, label_text) in enumerate(label_pairs):
      # Create a horizontal box to hold the button and label
      row = widgets.HBox([
          btn,
          widgets.HTMLMath(value=label_text)
      ])
      
      # Style the container with a border
      row.layout.border = '0px solid #444'
      row.layout.padding = '6px'
      row.layout.margin = '0px 0px'
      row.layout.align_items = 'center'  # vertical alignment
  
      display(row)
    
    
  def _render_MCS_question(self, q):
    self._inject_round_button_css()
  
    self.selected_answer = None
    self.option_buttons = []
    label_pairs = []
  
    for opt in q["options"]:
      btn = widgets.Button(
        description='',
        layout=widgets.Layout(width='20px', height='20px'),
        button_style=''
      )
      btn.layout.margin = '-4px 4px 0 0'
      btn.layout.align_self = 'center'
      btn.option_text = opt
      btn.add_class('round-button')
      self.option_buttons.append(btn)
  
      # Store button and raw LaTeX string
      label_pairs.append((btn, opt))
  
      def on_click(b, btn=btn):
        self.selected_answer = btn.option_text
        for other_btn in self.option_buttons:
          other_btn.description = ' '
          other_btn.button_style = ''
        btn.description = '✔️'
        btn.button_style = ''
  
      btn.on_click(on_click)
  
    return label_pairs

  # ---------- Rendering ----------
  def display_quiz(self):
    display(self._inject_code_css())
    with self.output:
      clear_output()
      self.message_label.value = ""
      self.feedback_label.value = ""
      self.answered_this_question = False
      self.current_answer_widgets = []

      q = self.questions[self.index]
      question_number = f"<b>Ερώτηση {self.index + 1}</b>"
      display(widgets.HTML(question_number))
      
      if q["type"] == "MCS":
        q["question"] = q["question"].replace(
          '<pre>',
          '<pre style="tab-size: 4; background-color: #ffe; border: 1px solid #ccc; color: black; padding:4px 6px; border-radius:4px; font-family:monospace;">')
        label_pairs = self._render_MCS_question(q)
        self.current_answer_widgets = [label_pairs]
        self.show_mathjax_question(q["question"], label_pairs);
      elif q["type"] == "SA":
        q["question"] = q["question"].replace(
          '<code>',
          '<code style="background-color:#f4f4f4; color:#c7254e; padding:4px 6px; border-radius:4px; font-family:monospace;">')
        sa_container = self._build_sa_widgets(q["question"])
        display(sa_container)

      # Enable/disable navigation buttons
      self.prev_btn.disabled = (self.index == 0)
      self.next_btn.description = "Τερματισμός" if self.index == self.total - 1 else "Επόμενη"

      btns = widgets.HBox([self.prev_btn, self.submit_btn, self.next_btn])
      display(btns)
      display(self.message_label)
      display(self.feedback_label)


  # --- Buld the short answer question type (SA) so that it renders html tags ---
  def _build_sa_widgets(self, question_html):
    lines = re.split(r'(?:<br\s*/?>|\n)', question_html, flags=re.IGNORECASE)
    row_widgets = []
  
    in_pre_block = False
    pre_block_lines = []
  
    for line in lines:
      # Detect start of <pre>
      if '<pre' in line:
        in_pre_block = True
        pre_block_lines = [line]
        continue
  
      # Detect end of </pre>
      if '</pre>' in line:
        in_pre_block = False
        pre_block_lines.append(line)
  
        # Process the collected pre block
        pre_widgets = []
        for pre_line in pre_block_lines:
          parts = pre_line.split('___')
          row_children = []
          for i, part in enumerate(parts):
            if part:
              row_children.append(widgets.HTML(value=part))
            if i < len(parts) - 1:
              tb = AutoResizingInput().get_widget()
              self.current_answer_widgets.append(tb)
              row_children.append(
                widgets.Box([tb], layout=widgets.Layout(display='inline-flex', align_items='baseline'))
              )
          pre_widgets.append(
            widgets.HBox(row_children, layout=widgets.Layout(flex_flow='row wrap', align_items='baseline'))
          )
  
        # Wrap the whole pre block in a styled VBox
        code_box = widgets.VBox(pre_widgets, layout=widgets.Layout(gap='2px'))
        self._inject_codebox_css()
        code_box.add_class("py-code")
        row_widgets.append(code_box)
        continue
  
      # If inside <pre>, collect lines
      if in_pre_block:
        pre_block_lines.append(line)
        continue
  
      # Normal line outside <pre>
      parts = line.split('___')
      row_children = []
      for i, part in enumerate(parts):
        if part:
          row_children.append(widgets.HTML(value=part))
        if i < len(parts) - 1:
          tb = AutoResizingInput().get_widget()
          self.current_answer_widgets.append(tb)
          row_children.append(
            widgets.Box([tb], layout=widgets.Layout(display='inline-flex', align_items='baseline'))
          )
      if not row_children:
        row_children = [widgets.HTML(value="")]
      row_widgets.append(
        widgets.HBox(row_children, layout=widgets.Layout(flex_flow='row wrap', align_items='baseline'))
      )
  
    return widgets.VBox(row_widgets, layout=widgets.Layout(gap='6px'))

  # ---------- Actions ----------
  def submit_answer(self, _):
    if self.answered_this_question:
      return

    q = self.questions[self.index]

    if q["type"] == "MCS":
      user_ans = self.selected_answer
      if user_ans is None:
        self.message_label.value = (
          "<span style='color:#c00;'>⚠️ Παρακαλώ επίλεξε μία απάντηση πριν συνεχίσεις</span>"
        )
        return
      correct = (user_ans == q["answer"])

    elif q["type"] == "SA":
      user_ans_list = [w.value for w in self.current_answer_widgets]
      if any(ans.strip() == "" for ans in user_ans_list):
        self.message_label.value = (
          "<span style='color:#c00;'>⚠️ Παρακαλώ πληκτρολογήστε μία απάντηση πριν συνεχίσετε.</span>"
        )
        return
      correct = self._check_sa_correct(q["answer"], user_ans_list)

    self.answered_this_question = True
    self.message_label.value = ""

    with self.output:
      clear_output(wait=True)
      qnum_html = f"<b>Ερώτηση {self.index + 1}</b>"
      display(widgets.HTML(qnum_html))

      if correct:
        # Feedback replaces question
        display(widgets.HTML("<span style='color:green; font-size:16px;'>✅ Σωστό!</span>"))

        if self.index not in self.scored_indices:
          self.score += 1
          self.scored_indices.add(self.index)

        # Disable submit button
        self.submit_btn.disabled = True
        btns = widgets.HBox([self.prev_btn, self.submit_btn, self.next_btn])

      else:
        # Feedback replaces question
        display(widgets.HTML("<span style='color:#c00; font-size:16px;'>❌ Λάθος.</span>"))

        # Re-enable submit (in case it was disabled before)
        self.submit_btn.disabled = False
        btns = widgets.HBox([self.prev_btn, self.retry_btn, self.next_btn])

      # Update navigation buttons
      self.prev_btn.disabled = (self.index == 0)
      self.next_btn.description = "Τερματισμός" if self.index == self.total - 1 else "Επόμενη"

      display(btns)
      display(self.message_label)
  
  def auto_advance(self):
    if self.index < self.total - 1:
      self.index += 1
      self.display_quiz()
    else:
      self.show_final_score()

  def retry_question(self, _):
    self.display_quiz()

  def prev_question(self, _):
    self.submit_btn.disabled = False
    if self.index > 0:
      self.index -= 1
      self.display_quiz()

  def next_or_finish(self, _):
    self.submit_btn.disabled = False
    if self.index < self.total - 1:
      self.index += 1
      self.display_quiz()
    else:
      self.show_final_score()

  def show_final_score(self):
    with self.output:
      clear_output()
      display(HTML(f"<h3>🎉 Τέλος κουίζ! Βαθμολογία: {self.score} από {self.total}</h3>"))

  # ---------- SA answer checking ----------
  def _check_sa_correct(self, correct_spec, user_answers):
    n_blanks = len(user_answers)
    norm = self._normalize_correct_spec(correct_spec, n_blanks)
    for ua, accepted in zip(user_answers, norm):
      if ua not in accepted:
        return False
    return True

  def _normalize_correct_spec(self, correct_spec, n_blanks):
    if isinstance(correct_spec, str):
      if n_blanks == 1:
        return [[correct_spec]]
      else:
        return [[correct_spec] for _ in range(n_blanks)]
    if isinstance(correct_spec, list):
      if n_blanks == 1:
        if all(isinstance(x, str) for x in correct_spec):
          return [correct_spec]
        if len(correct_spec) == 1 and isinstance(correct_spec[0], list):
          return [list(correct_spec[0])]
        return [[str(x) for x in correct_spec]]
      out = []
      for i in range(n_blanks):
        if i < len(correct_spec):
          item = correct_spec[i]
          if isinstance(item, list):
            out.append([str(x) for x in item])
          else:
            out.append([str(item)])
        else:
          out.append([])
      return out
    return [[] for _ in range(n_blanks)]