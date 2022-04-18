from flask import Flask, request

app = Flask(__name__)

clientes = [
			 	{"nome":"Jose", "email":"jose@gmail.com", "plano requisitado":"Drone de irrigação"},
			 	{"nome":"Claudio", "email":"claudio@gmail.com", "plano requisitado":"Drone de pulverização"},
			 	{"nome":"Lucas", "email":"lucas@gmail.com", "plano requisitado":"Drone de análise e irrigação"}
			 ]
@app.route("/")
def homepage():
  return "<h1>Pagina inicial -Agrobot-</h1>"

@app.route("/")
def cadastro():
  return "cadastro de clientes"

@app.route("/clientes")
def get_empregados():
	return {'clientes':clientes}

@app.route("/clientes/<plano>")
def get_clientes_plano(plano):
	out_clientes = []
	for cliente in clientes:
		if plano == clientes['plano requisitado'].lower():
			out_clientes.append(clientes)
	return {'clientes': out_clientes}

@app.route("/drones/planos")
def get_plano(drone):
	out_planos = []
	for plano in planos:
		if drone == plano['drone'].lower():
			out_planos.append(drone)
	return {'plano': out_planos}

  
user_data = {
1: {"Id": 0, "Nome": "Joao"},
2: {"Id": 1, "Nome": "Maria"}  
}

@app.route("/usuarios")
def list_users():
  return {"users": list(user_data.values())}
  
@app.route("/usuarios", methods=["POST"])
def cadatro_usuario():
  body = request.json

  ids = list(user_data.keys())

  if ids:
    new_id = ids[-1] + 1
  else:
    new_id = 1 

  user_data[new_id] = {
    "Id": new_id, "Nome": body["Nome"]
  }

app.run(host="0.0.0.0")