# Convertify
Convertify is a web app takes in any text or article link and converts it to a Lo-Fi audio file. Users can also select the number of words they want to include in a search query to acquire the audio file.

It was created within 24 hours during the Technica 2020 Hackathon: The world's largest all-women and non-binary hackathon. Convertify won the Most Creative Data Hack (sponsored by Splunk) prize. 

## Inspiration
Cabin fever hits hard. And it's not the most pleasant. We were experiencing cabin fever and a bit of burnout as a result of the altered school schedule and delivery format and wanted to bring fun into our lives. Thus we created Convertify: a dose of randomness and novel experience to discover Youtube videos based on a link or given text.

## Build Details
We used Django for the backend and wrote Python scripts to access the YouTube API, scrape data from the web, analyze the text, and do audio processing (pydub and youtube_dl). On the front end, we used JavaScript, HTML, CSS, Bootstrap for the HTML components, particle.js to create a dynamic background. We also used the circular audio wave JS library to create audio visualizations in beat with the music. JavaScript was used to implement a way for users to add their own twist to the music using their keyboard as a tool to generate sampled electronic sounds.
