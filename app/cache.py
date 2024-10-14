from app import cache

def cache_task(task_id, task_data):
    cache.set(f"task:{task_id}", task_data)

def get_cached_task(task_id):
    return cache.get(f"task:{task_id}")

def delete_cached_task(task_id):
    cache.delete(f"task:{task_id}")
