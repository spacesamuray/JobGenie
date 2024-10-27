from openai import OpenAI

class SpeakWithGPT:

    def __init__(self,model="gpt-4o-mini",system_role="You are a helpful assistant") -> None:
        self.client = OpenAI()
        self.model = model
        self.system_role = system_role

    def prompt(self, prompt):
        """
        This function is responsible for handling tasks that are given to GPT
        :param prompt: desired prompt
        :return: it returns the response of chatgpt
        """
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": self.system_role,
                },
                {
                    "role": "user",
                    "content": f"{prompt}",
                }
            ]
        )
        return completion