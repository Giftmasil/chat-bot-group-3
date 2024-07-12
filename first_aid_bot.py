from gemini_api import GeminiAPI

class FirstAidBot:
    def __init__(self):
        self.gemini_api = GeminiAPI()

    def get_first_aid_advice(self, user_input):
        prompt = f"""
        You are a first aid advice bot. Provide concise and accurate first aid guidance for the following situation:

        {user_input}

        If the query is not related to first aid, politely inform the user that you can only answer first aid related questions.

        Important: Always advise calling emergency services for serious situations.
        """

        response = self.gemini_api.generate_response(prompt)
        return response
