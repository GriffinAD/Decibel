import asyncio

class Test:
    async def job():
        print('cancel_me(): before sleep')

        try:
            # Wait for 1 hour
            while True:
                await asyncio.sleep(1)
                print ("2")
                
        except asyncio.CancelledError:
            print('cancelled')
            raise
        finally:
            print('clean up')

async def main():
    # Create a "cancel_me" Task
    test=Test
    
    task = asyncio.create_task(test.job())

    # Wait for 1 second
    await asyncio.sleep(3)

    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("main(): cancel_me is cancelled now")

asyncio.run(main())
