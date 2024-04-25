from app.config import VERSION, SERVICE, AUTHOR
from app.models.info_model import Info


class InfoService:
    def get_info(self) -> Info:
        return Info(version=VERSION, service=SERVICE, author=AUTHOR)
