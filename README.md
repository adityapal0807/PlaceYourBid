# PlaceYourBid
An open place for bidding on products and creating bids with features like user authentication , Wishlist and winner announcement .

## Features

### 1. Authentication
- This website provides user authentication like creating a new account , logging in using an existing account , log out of the current session.
- The features of commenting and placing a bid are only possible if logged in.
- For test case
      ```bash
        $ username = user1
      ```

      ```bash
        $ password = user1
      ```         

### 2. Creating Auction

- The user would be able to create an auction as per wish.
- The user would be required to give a title, a brief description, an image if possible, and a starting bid price in order to place an auction.
-Further the user who created the auction would be able to close the auction whenever the user wants.

### 3. Bidding

- The bid has to be higher than the initial price,
- All the subsequent bids would remain anonymous.

### 4. Comment And Wishlist

- Any user can comment or add or remove an item from the wishlist required that the user is loggen in.
- The comment added would be displayed next to the product.

### 5. Result 

- Once the auction is closed by the user, the user with the highest bid wins the auction.
- Thus the item would be removed from the Active Listing section.

### How to Run This on Local Website

### To deploy this project run

```bash
  $ pip install -r requirements.txt
```

```bash
  $ python manage.py runserver
```


Woohoo!! Now the website is running on your local

