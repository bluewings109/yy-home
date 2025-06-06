import jwt
import time

class JWTService:
    @staticmethod
    def is_token_expired(token: str | None) -> bool:
        if token is None:
            return True

        # 디코드 시 verify=False로 하면 exp 검증 없이 payload만 추출 가능
        payload = jwt.decode(token, "", options={"verify_signature": False}) # pyright: ignore

        exp: int | None = payload.get("exp")
        now = int(time.time())

        if exp is None:
            return True

        if now >= exp:
            return True

        return False
