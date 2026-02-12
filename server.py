from fastmcp import FastMCP

# 1. Creamos el servidor con un nombre identificable
mcp = FastMCP(name="Mi Primer MCP Server")

# 2. Registramos una herramienta simple
@mcp.tool
def greet(name: str) -> str:
    """
    Saluda a la persona por nombre.
    """
    return f"¡Hola, {name}! 👋"

# 3. Arrancamos el servidor
if __name__ == "__main__":
    # El servidor responderá a clientes MCP
    mcp.run()
