# database.py

import os
from redis.asyncio import Redis # <-- RedisCluster 대신 Redis 임포트
# from redis.asyncio.cluster import ClusterNode # <-- 이 줄은 더 이상 필요 없으니 삭제

REDIS_HOST = os.getenv("REDIS_HOST", "redis") # Docker Compose 서비스 이름은 그대로 'redis'
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_DB = int(os.getenv("REDIS_DB", 0))

async def get_redis_client(): # 함수 이름도 get_redis_client로 변경
    r = None # r 초기화
    try:
        # 일반 Redis 클라이언트로 변경
        r = Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            db=REDIS_DB,
            decode_responses=True
        )
        await r.ping()
        print("Connected to Redis successfully!") # 메시지도 변경
        yield r
    except Exception as e:
        print(f"Failed to connect to Redis: {e}") # 메시지도 변경
        raise # 오류를 다시 발생시켜 FastAPI가 500 에러를 반환하게 합니다.
    finally:
        if r:
            await r.close()