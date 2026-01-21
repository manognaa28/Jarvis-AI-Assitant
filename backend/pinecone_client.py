from pinecone import Pinecone

pc = Pinecone(api_key="pcsk_4hJgcb_2mfQxsEt9ftYJJLFFZWZDQuPTdkdb12dutQroRKCEw3rBV4iNB1NXqzYFhPH94G")
index = pc.Index("jarvis-index")
