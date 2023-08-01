# LittleLemon Restaurant

**Static template**: /restaurant/

---

## API paths

| Path                             | Method | Requires Token | Description |
| -------------------------------- | ------ | -------------- | ----------- |
| /auth/users/                     | POST   | False | create new user(register) |
| /auth/token/login/               | POST   | False | get token for registered user |
| /restaurant/menu/                | GET    | False | list menu items |
| /restaurant/menu/                | POST   | True  | create new menu items |
| /restaurant/menu/*id*/           | GET    | False | retrieve single menuitem |
| /restaurant/menu/*id*/           | PUT, DELETE | True | alter/delete menu |
| /restaurant/booking/tables/      | GET    | True  | list bookings |
| /restaurant/booking/tables/      | POST   | True  | create booking |
| /restaurant/booking/tables/*id*/ | GET, PUT, DELETE | True | alter/delete booking |
