from openai import OpenAI
from dotenv import load_dotenv
import os
from time import sleep
from helpers import *
from selecionar_persona import *

load_dotenv()

cliente = OpenAI(api_key=os.getenv("API_KEY_OPENAI"))
modelo = "gpt-4"
contexto = carrega("Projeto---3573-128d8b517ec1e2613f7fa7926e277e4853d0d9b3\\dados\\ecomart.txt")

def criar_thread():
    return cliente.beta.threads.create()

def criar_assistente():
    assistente = cliente.beta.assistants.create(
        name="Atendente EcoMart",
        instructions = f"""
            Você é um chatbot de atendimento a clientes de um e-commerce. 
            Você não deve responder perguntas que não sejam dados do ecommerce informado!
            Além disso, adote a persona abaixo para responder ao cliente.
            
            ## Contexto
            {contexto}
            
            ## Persona
            
            {personas["neutro"]}
        """,
        model = modelo,
    )
    return assistente