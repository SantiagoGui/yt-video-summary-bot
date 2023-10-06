from youtube_transcript_api import YouTubeTranscriptApi
import openai
OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY

link = input("Enter the youtube video link: ")
parts = link.split("=", 1)
video_ID = parts[1].split('_')[0]


outls = []
tx = YouTubeTranscriptApi.get_transcript(f'{video_ID}', languages=['de', 'en', 'pt'])

for i in tx:
    outtxt = (i['text'])
    print(outtxt)
    outls.append(outtxt)

def resumo(outls): 
         response = openai.Completion.create(
                engine='text-davinci-003',
                prompt=f"Destaque os principais pontos do texto, e faça um breve resumo ao fim: {outls}",
                temperature=0.7,
                max_tokens= 2048,
                top_p=1,
                stop=None)
         
         x = response["choices"][0]['text'].strip()
         with open("file.txt", "a") as file:
             file.write(x)

resumo(outls)
