# Product Specifications - E-Shop Checkout

## Features
1. **Cart Functionality**:
   - Users can add items to the cart.
   - Supported items: Headphones ($50), Watch ($120), Speaker ($30).
   - Cart summary must update dynamically.

2. **Discount Codes**:
   - Code `SAVE15` applies a 15% discount on the subtotal (before shipping).
   - Invalid codes should show an error message.

3. **Shipping**:
   - **Standard**: Free (0$).
   - **Express**: Flat rate of $10.
   - Changing shipping method updates the total immediately.

4. **Payment**:
   - Supported methods: Credit Card, PayPal.
   - Payment is processed only if all form validations pass.

5. **User Details**:
   - Name, Email, and Address are mandatory fields.
