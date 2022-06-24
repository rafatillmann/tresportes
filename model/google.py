import responses
import googlemaps


class Google:
    def __init__(self):
        self.__base_url = 'https://maps.googleapis.com',
        self.__matrix_url = '/maps/api/distancematrix/json'
        self.key = "AIzaSyDAJE4tTlgb1IGiHDAzf_i30jmdIFzv1nA"
        self.client = googlemaps.Client(self.key)

    def request(self, origins, destinations):
        responses.add(
            responses.GET,
            f'{self.__base_url}{self.__matrix_url}',
            body='{"status":"OK","rows":[]}',
            status=200,
            content_type="application/json",
        )

        return self.client.distance_matrix(
            origins, destinations, language='pt-br', region='bra')
