
from stocks.models import Stock


stocks_data = [
    {"symbol": "LLY", "company_name": "Eli Lilly and Company",
     "description": "Global pharmaceutical company focused on discovering and developing medicines for diabetes, oncology, immunology, and neuroscience.",
     "year_founded": 1876},

    {"symbol": "MSFT", "company_name": "Microsoft Corporation",
     "description": "Technology company producing software, hardware, and cloud services. Known for Windows, Office, and Azure cloud platform.",
     "year_founded": 1975},

    {"symbol": "NVDA", "company_name": "NVIDIA Corporation",
     "description": "Designs graphics processing units (GPUs) for gaming, AI, and professional visualization markets, and systems-on-a-chip for mobile devices.",
     "year_founded": 1993},

    {"symbol": "MDB", "company_name": "MongoDB, Inc.",
     "description": "Provides a general-purpose, document-based, distributed database platform used by modern applications.",
     "year_founded": 2007},

    {"symbol": "AMZN", "company_name": "Amazon.com, Inc.",
     "description": "E-commerce and cloud computing giant providing online retail, Amazon Web Services (AWS), and digital streaming services.",
     "year_founded": 1994},

    {"symbol": "AAPL", "company_name": "Apple Inc.",
     "description": "Technology company designing consumer electronics, software, and online services. Known for iPhone, Mac, iPad, and Apple Watch.",
     "year_founded": 1976},

    {"symbol": "BABA", "company_name": "Alibaba Group Holding Limited",
     "description": "Chinese multinational specializing in e-commerce, retail, internet, and technology services, including online marketplaces and cloud computing.",
     "year_founded": 1999},

    {"symbol": "COIN", "company_name": "Coinbase Global, Inc.",
     "description": "Cryptocurrency exchange platform allowing users to buy, sell, and store digital currencies like Bitcoin and Ethereum.",
     "year_founded": 2012},

    {"symbol": "PANW", "company_name": "Palo Alto Networks, Inc.",
     "description": "Cybersecurity company providing advanced firewalls and cloud-based security solutions for enterprises and service providers.",
     "year_founded": 2005},
]


for stock_data in stocks_data:
    stock, created = Stock.objects.get_or_create(
        symbol=stock_data["symbol"],
        defaults={
            "company_name": stock_data["company_name"],
            "description": stock_data["description"],
            "year_founded": stock_data["year_founded"],
        }
    )
    if created:
        print(f"Added {stock.symbol} - {stock.company_name}")
    else:
        print(f"{stock.symbol} already exists")
