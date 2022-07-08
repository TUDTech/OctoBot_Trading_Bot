class CommunityDonation:
    def __init__(self, amount: str, currency: str, blockchain: str, transaction_id: str, address_to: str):
        self.amount = amount
        self.currency = currency
        self.blockchain = blockchain
        self.transaction_id = transaction_id
        self.address_to = address_to

    def __str__(self):
        return f"{self.amount} {self.currency} on {self.blockchain} ({self.transaction_id})"

    @staticmethod
    def from_community_dict(data):
        data_attributes = data.get("attributes", {})
        return CommunityDonation(
            data_attributes.get("amount"),
            data_attributes.get("currency"),
            data_attributes.get("blockchain"),
            data_attributes.get("transaction_id"),
            data_attributes.get("address_to")
        )
