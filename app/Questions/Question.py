class Question:
    def __init__(self, question, category, format, subcategory=None, answer=None, options=None, examples=None, hints=None, explanation=None, image=None, ):
        self.question = question
        self.answer = answer
        self.options = options
        self.category = category
        self.examples = examples
        self.hints = hints
        self.explanation = explanation
        self.image = image
        self.subcategory = subcategory
        self.type = type
        self.format = format

    def __str__(self):
        return f'{self.question}'

    def check_answer(self, user_answer):
        return user_answer == self.answer

    def get_answer(self):
        return self.answer
    
    def get_type(self):
        return self.answer
    
    def get_format(self):
        return self.format
    
    def get_subcategory(self):
        return self.subcategory
    
    def get_image(self):
        return self.image
    
    def get_question(self):
        return self.question

    def get_options(self):
        return self.options
    
    def get_category(self):
        return self.category
    
    def get_examples(self):
        return self.examples
    
    def get_hints(self):
        return self.hints
    
    def get_explanation(self):
        return self.explanation

