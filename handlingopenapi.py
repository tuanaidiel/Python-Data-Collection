import openai

openai.api_key = "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"

try:
    question = input ("Enter your question: ")
    response = openai.completions.create(model = "gpt-3.5-turbo", prompt = question, max_tokens = 25)
    print (response)

except Exception as e:
    print (e)

