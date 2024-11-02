from speaak_with_gpt import SpeakWithGPT


class Selector:

    @staticmethod
    def select_titles(gpt_model : SpeakWithGPT, titles : list[dict[str,str]]) -> list[dict[str,str]]:
        """
        This method is responsible for selecting applications that are useful for user
        :param gpt_model:
        :param titles:
        :return: list[dict[str,str]]
        """
        new_applications : list[dict[str,str]]= []
        for application in titles:
            if gpt_model.prompt(application).choices[0].message.content == '1':
                new_applications.append(application)
                print(application)
        return new_applications
    #todo implement functionality of this method
    @staticmethod
    def select_application(gpt_model : SpeakWithGPT,applications : list[dict[str,str]]):
        pass