from summarization import Summarization
from flask import Flask
bulk = """<!DOCTYPE html>
<html>
<style>
body {
  background-image: url('data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIAIIAuQMBIgACEQEDEQH/xAAaAAEBAQEBAQEAAAAAAAAAAAADAgEABwYF/8QAGRABAQEBAQEAAAAAAAAAAAAAAQACESES/8QAGQEAAwEBAQAAAAAAAAAAAAAAAAEDAgYF/8QAFxEBAQEBAAAAAAAAAAAAAAAAAAERAv/aAAwDAQACEQMRAD8A/B5cknLOXtvE0fLEkSxIPRJYknLkhrQpYkqUpByiSlJUpSbcokoSXlKQ3KJKUlShIblElCTJQk25RJQypQkKSjShJWhm3KJKElShIUlElPJGzkKSvtOWclSzlNzej5TyVLEg5RcpSXlKTa0SWJIlPIblEliSJSkNyiSlJUoSbcokoSZKEhuUSUMqUJ7DcokoSZI0mpKJpSRKUiKSiShJdRpNSUbTW2QpH3HLOSpTym5nRpYknzYkHKJKUlSlIa0XKUlSlIblCliSJQk25RpSkiUJCkokpSVKEm3KJKElaEhSUSUMqUJNSUTQkqUMKSiSjRJqhnFJRasr0Uw3K+95ZyTljmk5fR8pSVKeQ1KJKUlSlJtyiShJWhhuUaUJKlCQ3KJKWTRQk1JRpQyJQk1JRtGiRKGFJRaKGXRQwpBJQypQk1JRMaSpQkKQSWcrSnk1I9B5YknzYlJykokp5KlKQ1KJPaUkShIblGlCSpQk1JRJQkqUJDcElCStGpqwWo2VoYUg2hkaGakotUMjQwpKNoZGNJqQbQyaoYUg2mvVM1I9GSxJEpSi5GUSUJMhQw3KJo1KlCTblElDKkaTiso0j0StDCkoko1KkeoVlElCStGpqQSUMjQzUg2PUuo9QrBpHqRoYUg2jUmqGakE2VapnqkelpSkqUJRcdKJKElaEhSUSUJI0M1IJoSTVGoVgtUJJqjU1INjSRoYV5HojSTVDNWD1HqVj1CkG0ak1HqasG0JJqNhSDaNSajZq8j1ZU0wpHp6UaJNUNFxkE0Mmo9TVg9Uak1GwpB6oa9UamrB6jZNRs1YjUbJqhhWDY2TVDNSDaNV6o1CsHqjVeqNTVg9RsjQwpB6oa2jU1IPVNbTCken6obLqLjYjUerrpq8o1G3XQpB6o1ddNWD1G23TVg9UN10KweqNXXTUg2jV10K8j1Rq66asHqNuuhSIaNXXTUiGm66FI//2Q==');
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
}
</style>
<body>
<pre>
<h1 style="text-align:center; color:white">hi</h1>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Sed tempus urna et pharetra. Nam libero justo laoreet sit amet cursus sit amet. 
Et leo duis ut diam quam nulla porttitor massa id. Volutpat consequat mauris nunc congue nisi vitae suscipit tellus. Enim ut sem viverra aliquet eget.
Ut diam quam nulla porttitor massa.
Eget magna fermentum iaculis eu non diam phasellus vestibulum. 
Faucibus pulvinar elementum integer enim neque. Adipiscing enim eu turpis egestas pretium aenean. Enim diam vulputate ut pharetra sit amet aliquam id diam.</p>

<p>Nibh nisl condimentum id venenatis a condimentum vitae. Neque viverra justo nec ultrices dui. Mauris in aliquam sem fringilla ut morbi tincidunt augue.
Turpis cursus in hac habitasse platea dictumst quisque sagittis. Justo nec ultrices dui sapien eget mi proin sed libero. Neque egestas congue quisque egestas diam in arcu.
Proin sagittis nisl rhoncus mattis rhoncus. 
Pellentesque diam volutpat commodo sed egestas egestas fringilla phasellus. Pulvinar elementum integer enim neque volutpat ac tincidunt vitae.
Lectus urna duis convallis convallis tellus. Fermentum iaculis eu non diam phasellus vestibulum lorem.
Arcu vitae elementum curabitur vitae nunc. 
Blandit aliquam etiam erat velit scelerisque. Quis eleifend quam adipiscing vitae proin sagittis nisl rhoncus.
Pharetra pharetra massa massa ultricies mi.</p>
</pre>
</body>

</html>

"""

app = Flask(__name__)

@app.route("/")
def home():

    return bulk


while(1):
    if __name__ == "__main__":
        app.run()
