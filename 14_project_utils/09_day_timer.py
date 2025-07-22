import time

def main():
    print("****************** Timer *****************\n")
    while True:
        try:
            time_input = int(input("Enter the Time in seconds: \n"))
            if time_input < 1:
                print("Invalid Input\n")
                continue
            
            print(f"Printer started for {time_input} Seconds.")
            
            for remaining in range(time_input,-1,-1):
                    minutes, seconds = divmod(remaining,60)
                    time_format = f"{minutes:02d}:{seconds:02d}"
                    print(time_format, end="\r")
                    time.sleep(1)
                    
            
            print("\nTime's up!\a")  # \a is optional "beep"

            break  # Exit after successful countdown
            
            
        except ValueError:
            print("Invalid Integer")
            
        except Exception as e:
            print(f"Error: {e}")
        

if __name__ == "__main__":
    main()