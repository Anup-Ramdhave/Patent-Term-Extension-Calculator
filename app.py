from flask import Flask, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/calculate-pte', methods=['POST'])
def calculate_patent_term_extension():
    data = request.get_json()
    # Extract the necessary data from the request payload
    patent_number = data['patentNumber']
    ind_filing_date = data['indFilingDate']
    patent_issuance_date = data['patentIssuanceDate']
    nda_submission_date = data['ndaSubmissionDate']
    nda_approval_date = data['ndaApprovalDate']
    original_expiration_date = data['originalExpirationDate']

    # Calculation logic here (use the existing calculate_patent_term_extension function)

    # Prepare the response data
    response = {
        'patent_number': patent_number,
        'original_expiration_date': original_expiration_date,
        'pte_years': pte.days / 365.25,
        'pte_days': pte.days,
        'final_expiration_date': final_expiration_date.strftime("%m/%d/%Y")
    }

    return jsonify(response)

# Run the Flask app
if __name__ == '__main__':
    app.run()