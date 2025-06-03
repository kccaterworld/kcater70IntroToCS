articleSummary = '''This paper investigates public understanding of AI ethics by analyzing Wikipedia data. The researchers used community detection algorithms to identify the hierarchical structure of AI ethics-related knowledge on the platform. Key findings reveal prominent themes such as corporate responsibility, theoretical underpinnings of AI ethics, ethical considerations for automated systems, and issues like copyright infringement. The study highlights the potential of using Wikipedia to gauge public awareness and improve education on AI ethics. While providing a structured overview of public concerns, the authors acknowledge limitations in relying solely on English Wikipedia content and the difficulty in establishing causal relationships. Ultimately, the research aims to enhance public knowledge of AI ethics to mitigate potential risks.'''
head = f'''<title>The Ethics of AI</title>
        <meta charset="UFT-8">
        <meta name="description" content="A summary of an AI article">
        <meta name="keywords" content="AI">
        <meta name="author" content="Kemal Cater">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" type="text/css" href="CSS/AI.css">'''

body = f'''<h1>Mapping Public Understanding of AI Ethics on Wikipedia</h1>
        <p>This study looked at people's understanding of the ethics behind AI by looking at wikipedia pages.</p>
        <h2>NotebookLM Summary:</h2>
        <audio controls>
            <source src="Mapping_Public_Understanding_of_AI_Ethics_on_Wikipedia.wav" type="audio/wav">
        Your browser does not support the audio element.
        </audio>
        <p>{articleSummary}<p>'''

page = f'''<!DOCTYPE html>
<html>
    <head> 
        {head}
    </head>
    <body>
        {body}
    </body>
</html>'''

with open("235824331.html","w") as file:
    file.write(page)
    file.close