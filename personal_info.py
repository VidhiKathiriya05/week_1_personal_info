def main():
    print("="*40)
    print("Welcome to the Personal Information App!")
    print("="*40)


    name = "Vidhi Kathiriya"
    age = 20
    city = "Ahmedabad"
    hobby = "reading books with suspense, crime, and horror"

    age_in_months = age * 12


    fav_food = input("Please enter your favorite food: ").strip()
    while not fav_food:
      print(">> Error: Input cannot be empty. Please try again.")
      fav_food = input("Please enter your favorite food: ").strip()

    fav_color = input("Please enter your favorite color: ").strip()
    while not fav_color:
      print(">> Error: Input cannot be empty. Please try again.")
      fav_color = input("Please enter your favorite color: ").strip()

    print("\n" + "="*40)
    print("      PROFILE SUMMARY")
    print("="*40)

    print(f"Name:           {name}")
    print(f"Location:       {city}")
    print(f"Age (Years):    {age}")
    print(f"Age (Months):   {age_in_months}")
    print(f"Hobby:          {hobby}")

    print("=" * 40)

    print(f"Favorite Food:  {fav_food}")
    print(f"Favorite Color: {fav_color}")
    print("="*40 + "\n")

    print("Data processed successfully. Goodbye!")

if __name__ == "__main__":
    main()