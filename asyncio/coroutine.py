import asyncio

async def task(name, delay):
    print(f"Task {name} started")
    await asyncio.sleep(delay)
    print(f"Task {name} done")

async def main():
    # Run both tasks at the same time
    await asyncio.gather(
        task("A", 2),
        task("B", 3)
    )

asyncio.run(main())
