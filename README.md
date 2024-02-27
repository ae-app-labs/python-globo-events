# globo-events
An web application that uses the Ticketmaster Discovery API to fetch events happening near a city.

## Stack

### Front End
- HTML
- Javascript
- CSS
- Bulma.io

### Back End
- Flask
- REST API Endpoint
- Communicate with Ticketmaster

### Ticketmaster
- Data source for events

## Config
Create a file named `.env` in the src folder.
[Discovery API](https://developer.ticketmaster.com/products-and-docs/apis/discovery-api/v2/)

```properties
API_KEY=<TICKETMASTER_API_KEY>
MOCK_RESPONSE=<true or false>
```