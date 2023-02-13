
# pip install revChatGPT
# python3 -m revChatGPT.Official --api_key API_KEY --stream

class chatGPT:
    @classmethod
    def ask(cls, prompt):
        import openai
        # Set up the OpenAI API client
        from configparser import ConfigParser
        cfg = ConfigParser()
        cfg.read('config.ini')
        api_key = cfg.get('openai', 'api_key')
        openai.api_key = api_key
        # Set up the model and prompt
        model_engine = "text-davinci-003"
        # prompt = "你好人生的意义上是什么?"
        # Generate a response
        # https://platform.openai.com/docs/api-reference/completions/create
        completion = openai.Completion.create(
            model=model_engine,
            prompt=prompt,
            # max_tokens=1024,
            # n=1,
            # stop=None,
            # temperature=0.5,
            temperature=0.3,
            max_tokens=2048,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        response = completion.choices[0].text.strip()
        print(response)
        return response
