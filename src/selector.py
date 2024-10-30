from speaak_with_gpt import SpeakWithGPT


class Selector:

    @staticmethod
    def select_titles(gpt_model : SpeakWithGPT,applications : list[dict[str,str]]) -> list[dict[str,str]]:
        new_applications : list[dict[str,str]]= []
        for application in applications:
            if gpt_model.prompt(application).choices[0].message.content == '1':
                new_applications.append(application)
                print(application)
        return new_applications