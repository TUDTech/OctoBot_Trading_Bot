import octobot.community.community_donation as community_donation
import octobot_commons.support as support


class CommunitySupports(support.Support):
    DEFAULT_SUPPORT_ROLE = "default"

    def __init__(self, support_role: str = None, donations: list = None):
        self.support_role = support_role or CommunitySupports.DEFAULT_SUPPORT_ROLE
        self.donations = donations or []

    def is_supporting(self) -> bool:
        return self.support_role != self.DEFAULT_SUPPORT_ROLE or bool(self.donations)

    @staticmethod
    def from_community_dict(data):
        return CommunitySupports(
            data["data"]["attributes"].get("support_role", CommunitySupports.DEFAULT_SUPPORT_ROLE),
            [community_donation.CommunityDonation.from_community_dict(donation_data)
             for donation_data in data.get("included", [])]
        )
