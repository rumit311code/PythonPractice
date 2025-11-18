# Install: pip install gql requests

from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

# Example public GraphQL endpoint
transport = RequestsHTTPTransport(url="https://countries.trevorblades.com/")
client = Client(transport=transport, fetch_schema_from_transport=True)

query = gql("""
    query {
      country(code: "IN") {
        name
        capital
        currency
      }
    }
""")

result = client.execute(query)
print(result)
