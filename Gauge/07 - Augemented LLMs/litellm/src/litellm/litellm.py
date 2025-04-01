from crewai.flow import Flow, listen, start
from litellm import completion


class LiteLLMFlow(Flow):
    
    @start
    def start_function(self):
        output = completion(
            model="gemini/gemini-1.5-flash",
            messages=[
                {'role':'user', 
                 'content':'Who is the founder of Pakistan?'}
                ]
        )
        return output ['choices'][0]['message']['content']

def run():
    obj = LiteLLMFlow()
    result = obj.kickoff() 
    print(result)