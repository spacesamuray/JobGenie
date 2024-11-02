from speaak_with_gpt import SpeakWithGPT


class Selector:

    @staticmethod
    def select_titles(gpt_model : SpeakWithGPT, titles : list[dict[str,str]]) -> list[dict[str,str]]:
        """
        This method is responsible for selecting titles that are useful for user
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

    #this method is useless bc of my mistake in WebScraper class where I don't considered this case
    #to make this method useful we need to change how WebScraper class operates more specifically turning bs4 objects into lists
    #methods: turn_applications_into_list(),turn_titles_into_list()
    @staticmethod
    def analyze_data(gpt_model : SpeakWithGPT,applications : list[dict[str,str]]):
        evaluated_data : list[dict[str,str]] = []
        for application in applications:
            response = gpt_model.prompt(application).choices[0].message.content
            if response != '1':
                pass

    @staticmethod
    def select_application(gpt_model : SpeakWithGPT,applications : list[dict[str,str]]):
        """
        This method is responsible for selecting applications that are useful for user
        and fetching emails from plane string
        :param gpt_model:
        :param applications:
        :return:
        """
        emails : list[dict[str,str]] = []
        for application in applications:
            response = gpt_model.prompt(application).choices[0].message.content
            if response != '0':
                item = {
                    "title": application["title"],
                    "email": response,
                }
                emails.append(item)
        return emails
