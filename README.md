# Akıllı-RAG-Ajanı (Yeni Proje)

# Bu projede Gemini kullanılmaktadır. Python sanal makina kurmanız gerekmektedir.
# python -m venv .venv

# Bu sistem, kullanıcıdan gelen soruları alır ve Gemini 2.0 Flash modeli ile işleyerek
# bağlama dayalı akıllı cevaplar üretir. Ayrıca TavilySearchResults aracı ile ilgili aramalar yapılabilir.

# Bu projede iki farklı kullanım örneği bulunmaktadır:
# 1) Hafıza Olmadan:
#    - Sadece tek seferlik sorgular için uygundur.
#    - create_react_agent(model, tools) ile agent çalıştırılır.
#    - Önceki sorgular hatırlanmaz, her sorgu bağımsızdır.

# 2) Hafıza ile:
#    - SqliteSaver kullanılarak thread bazlı hafıza tutulur.
#    - create_react_agent(model, tools, checkpointer=memory) ile agent çalıştırılır.
#    - Aynı thread içindeki tekrar sorular işlenebilir.
#    - UUID ile thread oluşturulur ve sorgular bağlanır.

# Model: gemini-2.0-flash
# Temperature: 0.7
# Tavily arama sonuçları: maksimum 2
# Hafıza (opsiyonel): Sqlite in-memory

# Bazı durumlarda Tavily aracı ilk sorgudan sonra tekrar kullanılmayabilir.
# Soruları İngilizce sormak, modelin daha doğru yanıt vermesini sağlar.

# Ortam Değişkenleri (.env)
"""
GEMINI_API_KEY=your_api_key
LANGCHAIN_API_KEY=your_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=AGENT
TAVILY_API_KEY=your_key
"""

# .env dosyasını kaydedin ve ana Python dosyasını çalıştırmadan önce yükleyin.
