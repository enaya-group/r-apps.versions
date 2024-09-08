from flask import Flask, jsonify

app = Flask(__name__)
app_latest_version = '1.1.13'

@app.route('/latest_version')
def latest_version():
    return jsonify({
        'version': '1.0.1',
        'download_url': f"rCashUp-{app_latest_version}-arm64-v8a_armeabi-v7a-release.apk?ref_type=heads&inline=false",
        'site': 'https://r-cashup.com/',
    })

if __name__ == '__main__':
    app.run(debug=True)

# NAY