from fastmcp import FastMCP

mcp = FastMCP("MiServer")

@mcp.tool
def suma(a: int, b: int) -> int:
    return a + b

# Bloque __main__ es opcional
if __name__ == "__main__":
    mcp.run()
