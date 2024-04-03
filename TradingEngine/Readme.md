#ReadMe

This package is deployed to a self hosted server using SSH and was a project to investigate hardware problems with high frequency trading systems

Scope of this project is to connect to an exchange and place orders in a systematic way.
- Connect to exchange to query data
- Execute trades 
- Monitor positions to manage a portfolio

## extensions
- Using cython to speed up exection
- Using Asyncio to help reduce delay in API calls