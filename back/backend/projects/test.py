import requests


def get_care_instructions(crop,temperature,soil_moisture,humidity):
    url = "https://gemini-pro-ai.p.rapidapi.com/"

    payload = { "contents": [
        {
			"role": "user",
			"parts": [{ "text": f"Hello. Give exact description for growing {crop} using less than 40 words under the folloing conditions temperature={temperature} soil_moisture={soil_moisture} humidity={humidity}" }]
		}
    ] }
    
    headers = {
	"x-rapidapi-key": "857bec4be2msh29993d5fa304af8p1ffff1jsn5ded8251ad87",
	"x-rapidapi-host": "gemini-pro-ai.p.rapidapi.com",
	"Content-Type": "application/json"
}
    response = requests.post(url, json=payload, headers=headers)
            
    return response.json()['candidates'][0]['content']['parts'][0]['text']

    