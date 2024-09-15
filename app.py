from flask import Flask, request, jsonify
import importlib

app = Flask(__name__)
app_latest_version = '1.1.13'

@app.route('/latest_version')
def latest_version():
    return jsonify({
        'version': str(app_latest_version),
        'download_url': f"rCashUp-{app_latest_version}.apk?ref_type=heads&inline=false",
        'site': 'https://r-cashup.com/get_r-cashup.html',
    })

# call like: GET /get_operation_options?sim=airtel&operation=retrait
@app.route('/get_operation_options', methods=['GET'])
def get_operation_options():
    # Retrieve the 'sim' parameter to locate the file and class
    sim = request.args.get('sim')
    # Retrieve the 'operation' parameter to locate the method to call
    operation = request.args.get('operation')
    
    if not sim:
        return jsonify({"error": "Parameter 'sim' is required"}), 400
    
    if not operation:
        return jsonify({"error": "Parameter 'operation' is required"}), 400
    
    try:
        # Dynamically import the module based on the sim param (assume module name = sim)
        module = importlib.import_module(sim.lower())
        
        # Assuming the class inside the module is named exactly like the sim parameter
        sim = request.args.get('sim').capitalize()
        ClassToCall = getattr(module, sim)
        
        # Dynamically get the method from the class
        operation = f"get_{operation}_options"
        method_to_call = getattr(ClassToCall(), operation)

        if not callable(method_to_call):
            return jsonify({"error": f"'{operation}' is not a valid method in class '{sim}'"}), 400
        
        # Call the method and get the result
        result = method_to_call()

        return jsonify({"result": result})
    
    except ModuleNotFoundError:
        return jsonify({"error": f"Module '{sim}' not found"}), 404
    except AttributeError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

# NAY