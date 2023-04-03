class ClaimNotification:
    def __init__(self, reference_number, claimant_email, claimant, notification_type):
        self.reference_number = reference_number
        self.claimant_email = claimant_email
        self.claimant = claimant
        self.notification_type = notification_type

    
    def claim_lodged(self):
        print(self.reference_number)


notif = ClaimNotification('1234', 'paulkadabo@gmail.com', 'Paul Ndambo', 'claim_lodged')
notif.claim_lodged()