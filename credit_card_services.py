from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from utils.config import Config

def analyze_credit_card(card_url):
        
    credential = AzureKeyCredential(Config.KEY)
        
    document_Client = DocumentIntelligenceClient(Config.ENDPOINT, credential)

    card_info = document_Client.begin_analyze_document(
        "prebuilt-creditCard", AnalyzeDocumentRequest(url_source=card_url))
    result = card_info.result()
        
    for document in result.documents:
        fields = document.get('fields', {})

        return {
            "card name": fields.get("CardHolderName", {}).get("content"),
            "bank_name": fields.get("IssuingBank", {}).get("content"),
            "expire_date": fields.get("ExpirationDate", {}).get("content"),
            "card_number": fields.get("CardNumber", {}).get("content"),
        }

    