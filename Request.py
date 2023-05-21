class Request: 
    def __init__(self, 
                 property: str, 
                 password: str, 
                 apt: str, 
                 vehicleMake: str,
                 vehicleModel: str, 
                 vehicleLicense: str,
                 email: str
                 ) -> None:
        self.property = property
        self.password = password
        self.apt = apt
        self.vehicleMake = vehicleMake
        self.vehicleModel = vehicleModel
        self.vehicleLicense = vehicleLicense
        self.email = email