from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
import random
import string
from dotenv import load_dotenv
import os

load_dotenv('token.env')
token = os.getenv("TOKEN")
url = "https://dropmail.me/api/graphql/" + token

def create_client():
  transport = AIOHTTPTransport(url=url)
  client = Client(transport=transport, fetch_schema_from_transport=True)
  return client

def get_domains():
  client = create_client()
  query = gql("query {domains {id, name, introducedAt, availableVia}}")
  return client.execute(query)

def get_session():
  client = create_client()
  query = gql("mutation {introduceSession {id, expiresAt, addresses {address}}}")
  return client.execute(query)

def list_sessions():
  client = create_client()
  query = gql("query {sessions {id, expiresAt, mails {rawSize, fromAddr, toAddr, downloadUrl, text, headerSubject}}}")
  return client.execute(query)

def get_mail(sessionId,domainId):
  client = create_client()
  query = gql("mutation ($input: IntroduceAddressInput!) {introduceAddress(input: $input) {address, restoreKey}}")
  variable_values={"input":{"sessionId":sessionId,"domainId":domainId}}
  return client.execute(query,variable_values=variable_values)

def list_mails(id):
  client = create_client()
  query = gql("query ($id: ID!) {session(id:$id) { addresses {address}, mails{rawSize, fromAddr, toAddr, downloadUrl, text, headerSubject}} }")
  variable_values={"id":id}
  return client.execute(query,variable_values=variable_values)

def generate_mail(base_address):
  def generate_random_string():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(random.randint(4, 6)))
  username, domain = base_address.split("@")
  extended_address = f"{username}.{generate_random_string()}@{generate_random_string()}.{domain}"
  return extended_address
