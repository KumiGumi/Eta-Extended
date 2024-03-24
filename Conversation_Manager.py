python
from anthropic_api import generate_response

class ConversationManager:
	def __init__(self):
		self.conversation_state = {}
		self.topic_stack = {}
		
	def process_input(self, text, ui_elements):
		#TODO: Analyze input, update conversation state pass
		
	def generate_response(self):
		prompt = self._build_prompt()
        response = generate_response(prompt)
        return response
		
	def update_topic(self, new_topic):
		self.topic_stack.append(new_topic)
	
	def switch_topic(self):
		if self.topic_stack:
			self.topic_stack.pop()
            
    def generate_response (self):
        prompt = self.build_prompt()
        response = generate_response(prompt)
        return response
        
    def _build_prompt(self):
        prompt = f"User: {self.conversation_state['user_input']}\n"
        prompt += f"Context: [self._summerize_context()\n"
        prompt += f"UI Elements: {self._describe_ui_elements()}\n"
        prompt += f"UI Elements: {self._describe_user_actions()}\n
        prompt += f"Assistant:"
        return prompt
        
    def _summerize_context(self):
        #TODO: Describe recent user actions
        pass
        
    def _describe_ui_elements(self):
        #TODO: Describe visible UI elements
        pass
    
    def _describe_user_actions(self):
        #TODO: Describe recent user action
        pass
    

 class UIElement:
    def __init__(self, type, text, bounds):
        self.type = type
        self.text = text
        self.bounds = bounds
        
class UserAction:
    def __init__(self, action_type, ui_element):
        self.action_type = action_type
        self.ui_element = ui_element
        
    