from travel import create_app

if __name__ == "__main__":    
    app = create_app()
    # Run on specific port and host to prevent chrome from blocking the request
    app.run(debug=True, host='0.0.0.0', port=3000)
