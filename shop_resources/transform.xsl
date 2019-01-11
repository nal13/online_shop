<?xml version="1.0" encoding="utf-8"?>

<xsl:stylesheet version="2.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:html="http://www.w3.org/1999/xhtml"
  >

  <xsl:strip-space elements="*"/>
  <xsl:output encoding="utf-8" indent="yes"/>

  <!-- root -->
  <xsl:template match="/">
    <!-- RDF prefixos -->
    <xsl:text disable-output-escaping="yes">@prefix loja: &lt;http://www.shop.pt/loja/&gt; . &#xa;</xsl:text>
    <xsl:text disable-output-escaping="yes">@prefix morada: &lt;http://www.shop.pt/morada/&gt; . &#xa;</xsl:text>
    <xsl:text disable-output-escaping="yes">@prefix contacto: &lt;http://www.shop.pt/contacto/&gt; . &#xa;</xsl:text>
    <xsl:text disable-output-escaping="yes">@prefix modelo: &lt;http://www.shop.pt/modelo/&gt; . &#xa;</xsl:text>
    <xsl:text disable-output-escaping="yes">@prefix modelo_em_loja: &lt;http://www.shop.pt/modelo/loja/&gt; . &#xa;</xsl:text>
    <xsl:text disable-output-escaping="yes">@prefix computador: &lt;http://www.shop.pt/modelo/computador/&gt; . &#xa;</xsl:text>
    <xsl:text disable-output-escaping="yes">@prefix telemovel: &lt;http://www.shop.pt/modelo/telemovel/&gt; . &#xa;</xsl:text>
    <xsl:text disable-output-escaping="yes">@prefix tablet: &lt;http://www.shop.pt/modelo/tablet/&gt; . &#xa;</xsl:text>
    <xsl:text disable-output-escaping="yes">@prefix camara: &lt;http://www.shop.pt/modelo/camara/&gt; . &#xa;</xsl:text>
    <xsl:text disable-output-escaping="yes">@prefix drone: &lt;http://www.shop.pt/modelo/drone/&gt; . &#xa;</xsl:text>
    <xsl:text disable-output-escaping="yes">@prefix tv: &lt;http://www.shop.pt/modelo/tv/&gt; . &#xa;</xsl:text>
    <xsl:text disable-output-escaping="yes">@prefix leitor_blueray: &lt;http://www.shop.pt/modelo/leitor_blueray/&gt; . &#xa;</xsl:text>
    <xsl:text disable-output-escaping="yes">@prefix maquina_cafe: &lt;http://www.shop.pt/modelo/maquina_cafe/&gt; . &#xa;</xsl:text>
    <xsl:text disable-output-escaping="yes">@prefix microondas: &lt;http://www.shop.pt/modelo/microondas/&gt; . &#xa;</xsl:text>
    <xsl:text disable-output-escaping="yes">@prefix maquina_lavar_roupa: &lt;http://www.shop.pt/modelo/maquina_lavar_roupa/&gt; . &#xa;</xsl:text>
    <xsl:text disable-output-escaping="yes">@prefix maquina_secar_roupa: &lt;http://www.shop.pt/modelo/maquina_secar_roupa/&gt; . &#xa;</xsl:text>
    <xsl:text disable-output-escaping="yes">@prefix aspirador: &lt;http://www.shop.pt/modelo/aspirador/&gt; . &#xa;</xsl:text>
    <xsl:text disable-output-escaping="yes">@prefix gaming_pc: &lt;http://www.shop.pt/modelo/gaming_pc/&gt; . &#xa;</xsl:text>
    <xsl:text disable-output-escaping="yes">@prefix consola: &lt;http://www.shop.pt/modelo/consola/&gt; . &#xa;</xsl:text>
    <xsl:text disable-output-escaping="yes">@prefix jogo: &lt;http://www.shop.pt/modelo/jogo/&gt; . &#xa;</xsl:text>
    <xsl:text disable-output-escaping="yes">@prefix cliente: &lt;http://www.shop.pt/cliente/&gt; . &#xa;</xsl:text>
    <xsl:text disable-output-escaping="yes">@prefix wishlist: &lt;http://www.shop.pt/cliente/wishlist/&gt; . &#xa;</xsl:text>
    <xsl:text disable-output-escaping="yes">@prefix cart: &lt;http://www.shop.pt/cliente/cart/&gt; . &#xa;</xsl:text>
    <xsl:text disable-output-escaping="yes">@prefix visited: &lt;http://www.shop.pt/cliente/visited/&gt; . &#xa;</xsl:text>
    <xsl:text disable-output-escaping="yes">&#xa;&#xa;&#xa;</xsl:text>

    <xsl:apply-templates/>
  </xsl:template>

  <xsl:template match="root/Lojas">

      <xsl:for-each select="Loja">
          <!-- Loja -->
          <!-- ID -->
          <xsl:text>loja:</xsl:text>
    			<xsl:value-of select="ID"/>
    			<xsl:text>&#xa;</xsl:text>

          <!-- tipo -->
          <xsl:text>&#9;a loja:</xsl:text>
    			<xsl:text> ; &#xa;</xsl:text>

          <!-- Nome -->
          <xsl:text>&#9;loja:nome "</xsl:text>
    			<xsl:value-of select="Nome"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- Image -->
          <xsl:text>&#9;loja:imagem "</xsl:text>
    			<xsl:value-of select="Imagem"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- Grupo -->
          <xsl:text>&#9;loja:grupo "</xsl:text>
    			<xsl:value-of select="Grupo"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- Morada -->
          <xsl:text>&#9;loja:morada </xsl:text>
    			<xsl:text>morada:</xsl:text>
          <xsl:value-of select="ID"/>
          <xsl:text> ; &#xa;</xsl:text>

          <!-- Contacto -->
          <xsl:text>&#9;loja:contacto </xsl:text>
    			<xsl:text>contacto:</xsl:text>
          <xsl:value-of select="ID"/>
          <xsl:text> . &#xa;</xsl:text>

          <!-- Morada -->
          <!-- ID -->
          <xsl:text>morada:</xsl:text>
    			<xsl:value-of select="ID"/>
    			<xsl:text>&#xa;</xsl:text>

          <!-- tipo -->
          <xsl:text>&#9;a morada:</xsl:text>
    			<xsl:text> ; &#xa;</xsl:text>

          <!-- Detalhes -->
          <xsl:text>&#9;morada:detalhes "</xsl:text>
    			<xsl:value-of select="Morada/Detalhes"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- Rua -->
          <xsl:text>&#9;morada:rua "</xsl:text>
    			<xsl:value-of select="Morada/Rua"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- CodigoPostal -->
          <xsl:text>&#9;morada:codigopostal "</xsl:text>
    			<xsl:value-of select="Morada/CodigoPostal"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- Distrito -->
          <xsl:text>&#9;morada:distrito "</xsl:text>
    			<xsl:value-of select="Morada/Distrito"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- Pais -->
          <xsl:text>&#9;morada:pais "</xsl:text>
    			<xsl:value-of select="Morada/Pais"/>
    			<xsl:text>" . &#xa;</xsl:text>

          <!-- Contacto -->
          <!-- ID -->
          <xsl:text>contacto:</xsl:text>
    			<xsl:value-of select="ID"/>
    			<xsl:text>&#xa;</xsl:text>

          <!-- tipo -->
          <xsl:text>&#9;a contacto:</xsl:text>
    			<xsl:text> ; &#xa;</xsl:text>

          <!-- Telefone -->
          <xsl:text>&#9;contacto:telefone "</xsl:text>
    			<xsl:value-of select="Contacto/Telefone"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- Fax -->
          <xsl:text>&#9;contacto:fax "</xsl:text>
    			<xsl:value-of select="Contacto/Fax"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- Email -->
          <xsl:text>&#9;contacto:email "</xsl:text>
    			<xsl:value-of select="Contacto/Email"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- Website -->
          <xsl:text>&#9;contacto:website "</xsl:text>
    			<xsl:value-of select="Contacto/Website"/>
    			<xsl:text>" . &#xa;&#xa;&#xa;</xsl:text>

      </xsl:for-each>

  </xsl:template>

  <xsl:template match="root/Produtos/Computadores">
      <xsl:for-each select="Modelo">
          <!-- Modelo -->
          <!-- ID -->
          <xsl:text>modelo:</xsl:text>
          <xsl:value-of select="ID"/>
          <xsl:text>&#xa;</xsl:text>

          <!-- tipo -->
          <xsl:text>&#9;a computador:</xsl:text>
    			<xsl:text> ; &#xa;</xsl:text>

          <!-- Nome -->
          <xsl:text>&#9;modelo:nome "</xsl:text>
    			<xsl:value-of select="Nome"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- Marca -->
          <xsl:text>&#9;modelo:marca "</xsl:text>
    			<xsl:value-of select="Marca"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- Categoria -->
          <xsl:text>&#9;modelo:categoria "</xsl:text>
    			<xsl:value-of select="Categoria"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- Ram -->
          <xsl:text>&#9;modelo:ram "</xsl:text>
    			<xsl:value-of select="Ram"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- Processador -->
          <xsl:text>&#9;modelo:processador "</xsl:text>
    			<xsl:value-of select="Processador"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- CapacidadeDisco -->
          <xsl:text>&#9;modelo:capacidadedisco "</xsl:text>
    			<xsl:value-of select="CapacidadeDisco"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- Gráfica -->
          <xsl:text>&#9;modelo:grafica "</xsl:text>
    			<xsl:value-of select="Grafica"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- TamanhoEcra -->
          <xsl:text>&#9;modelo:tamanhoecra "</xsl:text>
    			<xsl:value-of select="TamanhoEcra"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- Preco -->
          <xsl:text>&#9;modelo:preco "</xsl:text>
    			<xsl:value-of select="Preco"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Loja -->
          <xsl:text>&#9;modelo:loja </xsl:text>
          <xsl:for-each select="Loja">
              <xsl:text>modelo_em_loja:</xsl:text>
              <xsl:value-of select="../ID"/>
              <xsl:value-of select="ID"/>
              <xsl:choose>
                  <xsl:when test="position() != last()"> , &#xa;&#9;&#9;&#9;&#9;</xsl:when>
              </xsl:choose>
          </xsl:for-each>
          <xsl:text> . &#xa;</xsl:text>

          <xsl:for-each select="Loja">
            <!-- modelo_em_loja -->
            <!-- ID -->
            <xsl:text>modelo_em_loja:</xsl:text>
            <xsl:value-of select="../ID"/>
      			<xsl:value-of select="ID"/>
      			<xsl:text>&#xa;</xsl:text>

            <!-- Loja ID -->
            <xsl:text>&#9;modelo_em_loja:LojaID </xsl:text>
            <xsl:text>loja:</xsl:text>
      			<xsl:value-of select="ID"/>
            <xsl:text> ; &#xa;</xsl:text>

            <!-- Unidades -->
            <xsl:text>&#9;modelo_em_loja:unidades "</xsl:text>
      			<xsl:value-of select="Unidades"/>
            <xsl:text>" . &#xa;</xsl:text>
          </xsl:for-each>
          <xsl:text>&#xa;&#xa;</xsl:text>
      </xsl:for-each>
  </xsl:template>

  <xsl:template match="root/Produtos/Telemoveis">
      <xsl:for-each select="Modelo">
          <!-- Modelo -->
          <!-- ID -->
          <xsl:text>modelo:</xsl:text>
          <xsl:value-of select="ID"/>
          <xsl:text>&#xa;</xsl:text>

          <!-- tipo -->
          <xsl:text>&#9;a telemovel:</xsl:text>
    			<xsl:text> ; &#xa;</xsl:text>

          <!-- Nome -->
          <xsl:text>&#9;modelo:nome "</xsl:text>
    			<xsl:value-of select="Nome"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- Marca -->
          <xsl:text>&#9;modelo:marca "</xsl:text>
    			<xsl:value-of select="Marca"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- Categoria -->
          <xsl:text>&#9;modelo:categoria "</xsl:text>
    			<xsl:value-of select="Categoria"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- Ram -->
          <xsl:text>&#9;modelo:ram "</xsl:text>
    			<xsl:value-of select="Ram"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- Processador -->
          <xsl:text>&#9;modelo:processador "</xsl:text>
    			<xsl:value-of select="Processador"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- CapacidadeMemoria -->
          <xsl:text>&#9;modelo:capacidadememoria "</xsl:text>
    			<xsl:value-of select="CapacidadeMemoria"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- Camara -->
          <xsl:text>&#9;modelo:camara "</xsl:text>
    			<xsl:value-of select="Camara"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- TamanhoEcra -->
          <xsl:text>&#9;modelo:tamanhoecra "</xsl:text>
    			<xsl:value-of select="TamanhoEcra"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- Preco -->
          <xsl:text>&#9;modelo:preco "</xsl:text>
    			<xsl:value-of select="Preco"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Loja -->
          <xsl:text>&#9;modelo:loja </xsl:text>
          <xsl:for-each select="Loja">
              <xsl:text>modelo_em_loja:</xsl:text>
              <xsl:value-of select="../ID"/>
              <xsl:value-of select="ID"/>
              <xsl:choose>
                  <xsl:when test="position() != last()"> , &#xa;&#9;&#9;&#9;&#9;</xsl:when>
              </xsl:choose>
          </xsl:for-each>
          <xsl:text> . &#xa;</xsl:text>

          <xsl:for-each select="Loja">
            <!-- modelo_em_loja -->
            <!-- ID -->
            <xsl:text>modelo_em_loja:</xsl:text>
            <xsl:value-of select="../ID"/>
      			<xsl:value-of select="ID"/>
      			<xsl:text>&#xa;</xsl:text>

            <!-- Loja ID -->
            <xsl:text>&#9;modelo_em_loja:LojaID </xsl:text>
            <xsl:text>loja:</xsl:text>
      			<xsl:value-of select="ID"/>
            <xsl:text> ; &#xa;</xsl:text>

            <!-- Unidades -->
            <xsl:text>&#9;modelo_em_loja:unidades "</xsl:text>
      			<xsl:value-of select="Unidades"/>
            <xsl:text>" . &#xa;</xsl:text>
          </xsl:for-each>
          <xsl:text>&#xa;&#xa;</xsl:text>
      </xsl:for-each>
  </xsl:template>

  <xsl:template match="root/Produtos/Tablets">
      <xsl:for-each select="Modelo">
          <!-- Modelo -->
          <!-- ID -->
          <xsl:text>modelo:</xsl:text>
          <xsl:value-of select="ID"/>
          <xsl:text>&#xa;</xsl:text>

          <!-- tipo -->
          <xsl:text>&#9;a tablet:</xsl:text>
    			<xsl:text> ; &#xa;</xsl:text>

          <!-- Nome -->
          <xsl:text>&#9;modelo:nome "</xsl:text>
    			<xsl:value-of select="Nome"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- Marca -->
          <xsl:text>&#9;modelo:marca "</xsl:text>
    			<xsl:value-of select="Marca"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- Categoria -->
          <xsl:text>&#9;modelo:categoria "</xsl:text>
    			<xsl:value-of select="Categoria"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- Ram -->
          <xsl:text>&#9;modelo:ram "</xsl:text>
    			<xsl:value-of select="Ram"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- Processador -->
          <xsl:text>&#9;modelo:processador "</xsl:text>
    			<xsl:value-of select="Processador"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- CapacidadeMemoria -->
          <xsl:text>&#9;modelo:capacidadememoria "</xsl:text>
    			<xsl:value-of select="CapacidadeMemoria"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- Camara -->
          <xsl:text>&#9;modelo:camara "</xsl:text>
    			<xsl:value-of select="Camara"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- TamanhoEcra -->
          <xsl:text>&#9;modelo:tamanhoecra "</xsl:text>
    			<xsl:value-of select="TamanhoEcra"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- Preco -->
          <xsl:text>&#9;modelo:preco "</xsl:text>
    			<xsl:value-of select="Preco"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Loja -->
          <xsl:text>&#9;modelo:loja </xsl:text>
          <xsl:for-each select="Loja">
              <xsl:text>modelo_em_loja:</xsl:text>
              <xsl:value-of select="../ID"/>
              <xsl:value-of select="ID"/>
              <xsl:choose>
                  <xsl:when test="position() != last()"> , &#xa;&#9;&#9;&#9;&#9;</xsl:when>
              </xsl:choose>
          </xsl:for-each>
          <xsl:text> . &#xa;</xsl:text>

          <xsl:for-each select="Loja">
            <!-- modelo_em_loja -->
            <!-- ID -->
            <xsl:text>modelo_em_loja:</xsl:text>
            <xsl:value-of select="../ID"/>
      			<xsl:value-of select="ID"/>
      			<xsl:text>&#xa;</xsl:text>

            <!-- Loja ID -->
            <xsl:text>&#9;modelo_em_loja:LojaID </xsl:text>
            <xsl:text>loja:</xsl:text>
      			<xsl:value-of select="ID"/>
            <xsl:text> ; &#xa;</xsl:text>

            <!-- Unidades -->
            <xsl:text>&#9;modelo_em_loja:unidades "</xsl:text>
      			<xsl:value-of select="Unidades"/>
            <xsl:text>" . &#xa;</xsl:text>
          </xsl:for-each>
          <xsl:text>&#xa;&#xa;</xsl:text>
      </xsl:for-each>
  </xsl:template>

  <xsl:template match="root/Produtos/Camaras">
      <xsl:for-each select="Modelo">
          <!-- Modelo -->
          <!-- ID -->
          <xsl:text>modelo:</xsl:text>
          <xsl:value-of select="ID"/>
          <xsl:text>&#xa;</xsl:text>

          <!-- tipo -->
          <xsl:text>&#9;a camara:</xsl:text>
          <xsl:text> ; &#xa;</xsl:text>

          <!-- Nome -->
          <xsl:text>&#9;modelo:nome "</xsl:text>
          <xsl:value-of select="Nome"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Marca -->
          <xsl:text>&#9;modelo:marca "</xsl:text>
          <xsl:value-of select="Marca"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Categoria -->
          <xsl:text>&#9;modelo:categoria "</xsl:text>
          <xsl:value-of select="Categoria"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- ResolucaoVideo -->
          <xsl:text>&#9;modelo:resolucaovideo "</xsl:text>
          <xsl:value-of select="ResolucaoVideo"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Wireless -->
          <xsl:text>&#9;modelo:wireless "</xsl:text>
          <xsl:value-of select="Wireless"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- ResolucaoFoto -->
          <xsl:text>&#9;modelo:resolucaofoto "</xsl:text>
          <xsl:value-of select="ResolucaoFoto"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Preco -->
          <xsl:text>&#9;modelo:preco "</xsl:text>
          <xsl:value-of select="Preco"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Loja -->
          <xsl:text>&#9;modelo:loja </xsl:text>
          <xsl:for-each select="Loja">
              <xsl:text>modelo_em_loja:</xsl:text>
              <xsl:value-of select="../ID"/>
              <xsl:value-of select="ID"/>
              <xsl:choose>
                  <xsl:when test="position() != last()"> , &#xa;&#9;&#9;&#9;&#9;</xsl:when>
              </xsl:choose>
          </xsl:for-each>
          <xsl:text> . &#xa;</xsl:text>

          <xsl:for-each select="Loja">
            <!-- modelo_em_loja -->
            <!-- ID -->
            <xsl:text>modelo_em_loja:</xsl:text>
            <xsl:value-of select="../ID"/>
            <xsl:value-of select="ID"/>
            <xsl:text>&#xa;</xsl:text>

            <!-- Loja ID -->
            <xsl:text>&#9;modelo_em_loja:LojaID </xsl:text>
            <xsl:text>loja:</xsl:text>
      			<xsl:value-of select="ID"/>
            <xsl:text> ; &#xa;</xsl:text>

            <!-- Unidades -->
            <xsl:text>&#9;modelo_em_loja:unidades "</xsl:text>
            <xsl:value-of select="Unidades"/>
            <xsl:text>" . &#xa;</xsl:text>
          </xsl:for-each>
          <xsl:text>&#xa;&#xa;</xsl:text>
      </xsl:for-each>
  </xsl:template>

  <xsl:template match="root/Produtos/Drones">
      <xsl:for-each select="Modelo">
          <!-- Modelo -->
          <!-- ID -->
          <xsl:text>modelo:</xsl:text>
          <xsl:value-of select="ID"/>
          <xsl:text>&#xa;</xsl:text>

          <!-- tipo -->
          <xsl:text>&#9;a drone:</xsl:text>
          <xsl:text> ; &#xa;</xsl:text>

          <!-- Nome -->
          <xsl:text>&#9;modelo:nome "</xsl:text>
          <xsl:value-of select="Nome"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Marca -->
          <xsl:text>&#9;modelo:marca "</xsl:text>
          <xsl:value-of select="Marca"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Categoria -->
          <xsl:text>&#9;modelo:categoria "</xsl:text>
          <xsl:value-of select="Categoria"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Autonomia -->
          <xsl:text>&#9;modelo:autonomia "</xsl:text>
          <xsl:value-of select="Autonomia"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Raio -->
          <xsl:text>&#9;modelo:raio "</xsl:text>
          <xsl:value-of select="Raio"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- CamaraImb -->
          <xsl:text>&#9;modelo:camaraimb "</xsl:text>
          <xsl:value-of select="CamaraImb"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Preco -->
          <xsl:text>&#9;modelo:preco "</xsl:text>
          <xsl:value-of select="Preco"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Loja -->
          <xsl:text>&#9;modelo:loja </xsl:text>
          <xsl:for-each select="Loja">
              <xsl:text>modelo_em_loja:</xsl:text>
              <xsl:value-of select="../ID"/>
              <xsl:value-of select="ID"/>
              <xsl:choose>
                  <xsl:when test="position() != last()"> , &#xa;&#9;&#9;&#9;&#9;</xsl:when>
              </xsl:choose>
          </xsl:for-each>
          <xsl:text> . &#xa;</xsl:text>

          <xsl:for-each select="Loja">
            <!-- modelo_em_loja -->
            <!-- ID -->
            <xsl:text>modelo_em_loja:</xsl:text>
            <xsl:value-of select="../ID"/>
            <xsl:value-of select="ID"/>
            <xsl:text>&#xa;</xsl:text>

            <!-- Loja ID -->
            <xsl:text>&#9;modelo_em_loja:LojaID </xsl:text>
            <xsl:text>loja:</xsl:text>
      			<xsl:value-of select="ID"/>
            <xsl:text> ; &#xa;</xsl:text>

            <!-- Unidades -->
            <xsl:text>&#9;modelo_em_loja:unidades "</xsl:text>
            <xsl:value-of select="Unidades"/>
            <xsl:text>" . &#xa;</xsl:text>
          </xsl:for-each>
          <xsl:text>&#xa;&#xa;</xsl:text>
      </xsl:for-each>
  </xsl:template>

  <xsl:template match="root/Produtos/TVs">
      <xsl:for-each select="Modelo">
          <!-- Modelo -->
          <!-- ID -->
          <xsl:text>modelo:</xsl:text>
          <xsl:value-of select="ID"/>
          <xsl:text>&#xa;</xsl:text>

          <!-- tipo -->
          <xsl:text>&#9;a tv:</xsl:text>
          <xsl:text> ; &#xa;</xsl:text>

          <!-- Nome -->
          <xsl:text>&#9;modelo:nome "</xsl:text>
          <xsl:value-of select="Nome"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Marca -->
          <xsl:text>&#9;modelo:marca "</xsl:text>
          <xsl:value-of select="Marca"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Categoria -->
          <xsl:text>&#9;modelo:categoria "</xsl:text>
          <xsl:value-of select="Categoria"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- TamanhoEcra -->
          <xsl:text>&#9;modelo:tamanhoecra "</xsl:text>
          <xsl:value-of select="TamanhoEcra"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- QualidadeImagem -->
          <xsl:text>&#9;modelo:qualidadeimagem "</xsl:text>
          <xsl:value-of select="QualidadeImagem"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Frequencia -->
          <xsl:text>&#9;modelo:frequencia "</xsl:text>
          <xsl:value-of select="Frequencia"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Preco -->
          <xsl:text>&#9;modelo:preco "</xsl:text>
          <xsl:value-of select="Preco"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Loja -->
          <xsl:text>&#9;modelo:loja </xsl:text>
          <xsl:for-each select="Loja">
              <xsl:text>modelo_em_loja:</xsl:text>
              <xsl:value-of select="../ID"/>
              <xsl:value-of select="ID"/>
              <xsl:choose>
                  <xsl:when test="position() != last()"> , &#xa;&#9;&#9;&#9;&#9;</xsl:when>
              </xsl:choose>
          </xsl:for-each>
          <xsl:text> . &#xa;</xsl:text>

          <xsl:for-each select="Loja">
            <!-- modelo_em_loja -->
            <!-- ID -->
            <xsl:text>modelo_em_loja:</xsl:text>
            <xsl:value-of select="../ID"/>
            <xsl:value-of select="ID"/>
            <xsl:text>&#xa;</xsl:text>

            <!-- Loja ID -->
            <xsl:text>&#9;modelo_em_loja:LojaID </xsl:text>
            <xsl:text>loja:</xsl:text>
      			<xsl:value-of select="ID"/>
            <xsl:text> ; &#xa;</xsl:text>

            <!-- Unidades -->
            <xsl:text>&#9;modelo_em_loja:unidades "</xsl:text>
            <xsl:value-of select="Unidades"/>
            <xsl:text>" . &#xa;</xsl:text>
          </xsl:for-each>
          <xsl:text>&#xa;&#xa;</xsl:text>
      </xsl:for-each>
  </xsl:template>

  <xsl:template match="root/Produtos/LeitoresBlueray">
      <xsl:for-each select="Modelo">
          <!-- Modelo -->
          <!-- ID -->
          <xsl:text>modelo:</xsl:text>
          <xsl:value-of select="ID"/>
          <xsl:text>&#xa;</xsl:text>

          <!-- tipo -->
          <xsl:text>&#9;a leitor_blueray:</xsl:text>
          <xsl:text> ; &#xa;</xsl:text>

          <!-- Nome -->
          <xsl:text>&#9;modelo:nome "</xsl:text>
          <xsl:value-of select="Nome"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Marca -->
          <xsl:text>&#9;modelo:marca "</xsl:text>
          <xsl:value-of select="Marca"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Categoria -->
          <xsl:text>&#9;modelo:categoria "</xsl:text>
          <xsl:value-of select="Categoria"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- FormatosReproducao -->
          <xsl:text>&#9;modelo:formatosreproducao "</xsl:text>
          <xsl:value-of select="FormatosReproducao"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Resolucao -->
          <xsl:text>&#9;modelo:resolucao "</xsl:text>
          <xsl:value-of select="Resolucao"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Preco -->
          <xsl:text>&#9;modelo:preco "</xsl:text>
          <xsl:value-of select="Preco"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Loja -->
          <xsl:text>&#9;modelo:loja </xsl:text>
          <xsl:for-each select="Loja">
              <xsl:text>modelo_em_loja:</xsl:text>
              <xsl:value-of select="../ID"/>
              <xsl:value-of select="ID"/>
              <xsl:choose>
                  <xsl:when test="position() != last()"> , &#xa;&#9;&#9;&#9;&#9;</xsl:when>
              </xsl:choose>
          </xsl:for-each>
          <xsl:text> . &#xa;</xsl:text>

          <xsl:for-each select="Loja">
            <!-- modelo_em_loja -->
            <!-- ID -->
            <xsl:text>modelo_em_loja:</xsl:text>
            <xsl:value-of select="../ID"/>
            <xsl:value-of select="ID"/>
            <xsl:text>&#xa;</xsl:text>

            <!-- Loja ID -->
            <xsl:text>&#9;modelo_em_loja:LojaID </xsl:text>
            <xsl:text>loja:</xsl:text>
      			<xsl:value-of select="ID"/>
            <xsl:text> ; &#xa;</xsl:text>

            <!-- Unidades -->
            <xsl:text>&#9;modelo_em_loja:unidades "</xsl:text>
            <xsl:value-of select="Unidades"/>
            <xsl:text>" . &#xa;</xsl:text>
          </xsl:for-each>
          <xsl:text>&#xa;&#xa;</xsl:text>
      </xsl:for-each>
  </xsl:template>

  <xsl:template match="root/Produtos/MaquinasCafe">
      <xsl:for-each select="Modelo">
          <!-- Modelo -->
          <!-- ID -->
          <xsl:text>modelo:</xsl:text>
          <xsl:value-of select="ID"/>
          <xsl:text>&#xa;</xsl:text>

          <!-- tipo -->
          <xsl:text>&#9;a maquina_cafe:</xsl:text>
          <xsl:text> ; &#xa;</xsl:text>

          <!-- Nome -->
          <xsl:text>&#9;modelo:nome "</xsl:text>
          <xsl:value-of select="Nome"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Marca -->
          <xsl:text>&#9;modelo:marca "</xsl:text>
          <xsl:value-of select="Marca"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Categoria -->
          <xsl:text>&#9;modelo:categoria "</xsl:text>
          <xsl:value-of select="Categoria"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Cor -->
          <xsl:text>&#9;modelo:cor "</xsl:text>
          <xsl:value-of select="Cor"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Agua -->
          <xsl:text>&#9;modelo:agua "</xsl:text>
          <xsl:value-of select="Agua"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Potencia -->
          <xsl:text>&#9;modelo:potencia "</xsl:text>
          <xsl:value-of select="Potencia"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Preco -->
          <xsl:text>&#9;modelo:preco "</xsl:text>
          <xsl:value-of select="Preco"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Loja -->
          <xsl:text>&#9;modelo:loja </xsl:text>
          <xsl:for-each select="Loja">
              <xsl:text>modelo_em_loja:</xsl:text>
              <xsl:value-of select="../ID"/>
              <xsl:value-of select="ID"/>
              <xsl:choose>
                  <xsl:when test="position() != last()"> , &#xa;&#9;&#9;&#9;&#9;</xsl:when>
              </xsl:choose>
          </xsl:for-each>
          <xsl:text> . &#xa;</xsl:text>

          <xsl:for-each select="Loja">
            <!-- modelo_em_loja -->
            <!-- ID -->
            <xsl:text>modelo_em_loja:</xsl:text>
            <xsl:value-of select="../ID"/>
            <xsl:value-of select="ID"/>
            <xsl:text>&#xa;</xsl:text>

            <!-- Loja ID -->
            <xsl:text>&#9;modelo_em_loja:LojaID </xsl:text>
            <xsl:text>loja:</xsl:text>
      			<xsl:value-of select="ID"/>
            <xsl:text> ; &#xa;</xsl:text>

            <!-- Unidades -->
            <xsl:text>&#9;modelo_em_loja:unidades "</xsl:text>
            <xsl:value-of select="Unidades"/>
            <xsl:text>" . &#xa;</xsl:text>
          </xsl:for-each>
          <xsl:text>&#xa;&#xa;</xsl:text>
      </xsl:for-each>
  </xsl:template>

  <xsl:template match="root/Produtos/Microondas">
      <xsl:for-each select="Modelo">
          <!-- Modelo -->
          <!-- ID -->
          <xsl:text>modelo:</xsl:text>
          <xsl:value-of select="ID"/>
          <xsl:text>&#xa;</xsl:text>

          <!-- tipo -->
          <xsl:text>&#9;a microondas:</xsl:text>
          <xsl:text> ; &#xa;</xsl:text>

          <!-- Nome -->
          <xsl:text>&#9;modelo:nome "</xsl:text>
          <xsl:value-of select="Nome"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Marca -->
          <xsl:text>&#9;modelo:marca "</xsl:text>
          <xsl:value-of select="Marca"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Categoria -->
          <xsl:text>&#9;modelo:categoria "</xsl:text>
          <xsl:value-of select="Categoria"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Grill -->
          <xsl:text>&#9;modelo:grill "</xsl:text>
          <xsl:value-of select="Grill"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- VolumeMax -->
          <xsl:text>&#9;modelo:volumemax "</xsl:text>
          <xsl:value-of select="VolumeMax"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- PotenciaMax -->
          <xsl:text>&#9;modelo:potenciamax "</xsl:text>
          <xsl:value-of select="PotenciaMax"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Preco -->
          <xsl:text>&#9;modelo:preco "</xsl:text>
          <xsl:value-of select="Preco"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Loja -->
          <xsl:text>&#9;modelo:loja </xsl:text>
          <xsl:for-each select="Loja">
              <xsl:text>modelo_em_loja:</xsl:text>
              <xsl:value-of select="../ID"/>
              <xsl:value-of select="ID"/>
              <xsl:choose>
                  <xsl:when test="position() != last()"> , &#xa;&#9;&#9;&#9;&#9;</xsl:when>
              </xsl:choose>
          </xsl:for-each>
          <xsl:text> . &#xa;</xsl:text>

          <xsl:for-each select="Loja">
            <!-- modelo_em_loja -->
            <!-- ID -->
            <xsl:text>modelo_em_loja:</xsl:text>
            <xsl:value-of select="../ID"/>
            <xsl:value-of select="ID"/>
            <xsl:text>&#xa;</xsl:text>

            <!-- Loja ID -->
            <xsl:text>&#9;modelo_em_loja:LojaID </xsl:text>
            <xsl:text>loja:</xsl:text>
      			<xsl:value-of select="ID"/>
            <xsl:text> ; &#xa;</xsl:text>

            <!-- Unidades -->
            <xsl:text>&#9;modelo_em_loja:unidades "</xsl:text>
            <xsl:value-of select="Unidades"/>
            <xsl:text>" . &#xa;</xsl:text>
          </xsl:for-each>
          <xsl:text>&#xa;&#xa;</xsl:text>
      </xsl:for-each>
  </xsl:template>

  <xsl:template match="root/Produtos/MaquinaLavarRoupa">
      <xsl:for-each select="Modelo">
          <!-- Modelo -->
          <!-- ID -->
          <xsl:text>modelo:</xsl:text>
          <xsl:value-of select="ID"/>
          <xsl:text>&#xa;</xsl:text>

          <!-- tipo -->
          <xsl:text>&#9;a maquina_lavar_roupa:</xsl:text>
          <xsl:text> ; &#xa;</xsl:text>

          <!-- Nome -->
          <xsl:text>&#9;modelo:nome "</xsl:text>
          <xsl:value-of select="Nome"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Marca -->
          <xsl:text>&#9;modelo:marca "</xsl:text>
          <xsl:value-of select="Marca"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Categoria -->
          <xsl:text>&#9;modelo:categoria "</xsl:text>
          <xsl:value-of select="Categoria"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Eficiencia -->
          <xsl:text>&#9;modelo:eficiencia "</xsl:text>
          <xsl:value-of select="Eficiencia"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Capacidade -->
          <xsl:text>&#9;modelo:capacidade "</xsl:text>
          <xsl:value-of select="Capacidade"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- VelocidadeCen -->
          <xsl:text>&#9;modelo:velocidadecen "</xsl:text>
          <xsl:value-of select="VelocidadeCen"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Preco -->
          <xsl:text>&#9;modelo:preco "</xsl:text>
          <xsl:value-of select="Preco"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Loja -->
          <xsl:text>&#9;modelo:loja </xsl:text>
          <xsl:for-each select="Loja">
              <xsl:text>modelo_em_loja:</xsl:text>
              <xsl:value-of select="../ID"/>
              <xsl:value-of select="ID"/>
              <xsl:choose>
                  <xsl:when test="position() != last()"> , &#xa;&#9;&#9;&#9;&#9;</xsl:when>
              </xsl:choose>
          </xsl:for-each>
          <xsl:text> . &#xa;</xsl:text>

          <xsl:for-each select="Loja">
            <!-- modelo_em_loja -->
            <!-- ID -->
            <xsl:text>modelo_em_loja:</xsl:text>
            <xsl:value-of select="../ID"/>
            <xsl:value-of select="ID"/>
            <xsl:text>&#xa;</xsl:text>

            <!-- Loja ID -->
            <xsl:text>&#9;modelo_em_loja:LojaID </xsl:text>
            <xsl:text>loja:</xsl:text>
      			<xsl:value-of select="ID"/>
            <xsl:text> ; &#xa;</xsl:text>

            <!-- Unidades -->
            <xsl:text>&#9;modelo_em_loja:unidades "</xsl:text>
            <xsl:value-of select="Unidades"/>
            <xsl:text>" . &#xa;</xsl:text>
          </xsl:for-each>
          <xsl:text>&#xa;&#xa;</xsl:text>
      </xsl:for-each>
  </xsl:template>

  <xsl:template match="root/Produtos/MaquinaSecarRoupa">
      <xsl:for-each select="Modelo">
          <!-- Modelo -->
          <!-- ID -->
          <xsl:text>modelo:</xsl:text>
          <xsl:value-of select="ID"/>
          <xsl:text>&#xa;</xsl:text>

          <!-- tipo -->
          <xsl:text>&#9;a maquina_secar_roupa:</xsl:text>
          <xsl:text> ; &#xa;</xsl:text>

          <!-- Nome -->
          <xsl:text>&#9;modelo:nome "</xsl:text>
          <xsl:value-of select="Nome"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Marca -->
          <xsl:text>&#9;modelo:marca "</xsl:text>
          <xsl:value-of select="Marca"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Categoria -->
          <xsl:text>&#9;modelo:categoria "</xsl:text>
          <xsl:value-of select="Categoria"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Eficiencia -->
          <xsl:text>&#9;modelo:eficiencia "</xsl:text>
          <xsl:value-of select="Eficiencia"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Capacidade -->
          <xsl:text>&#9;modelo:capacidade "</xsl:text>
          <xsl:value-of select="Capacidade"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Consumo -->
          <xsl:text>&#9;modelo:consumo "</xsl:text>
          <xsl:value-of select="Consumo"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Preco -->
          <xsl:text>&#9;modelo:preco "</xsl:text>
          <xsl:value-of select="Preco"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Loja -->
          <xsl:text>&#9;modelo:loja </xsl:text>
          <xsl:for-each select="Loja">
              <xsl:text>modelo_em_loja:</xsl:text>
              <xsl:value-of select="../ID"/>
              <xsl:value-of select="ID"/>
              <xsl:choose>
                  <xsl:when test="position() != last()"> , &#xa;&#9;&#9;&#9;&#9;</xsl:when>
              </xsl:choose>
          </xsl:for-each>
          <xsl:text> . &#xa;</xsl:text>

          <xsl:for-each select="Loja">
            <!-- modelo_em_loja -->
            <!-- ID -->
            <xsl:text>modelo_em_loja:</xsl:text>
            <xsl:value-of select="../ID"/>
            <xsl:value-of select="ID"/>
            <xsl:text>&#xa;</xsl:text>

            <!-- Loja ID -->
            <xsl:text>&#9;modelo_em_loja:LojaID </xsl:text>
            <xsl:text>loja:</xsl:text>
      			<xsl:value-of select="ID"/>
            <xsl:text> ; &#xa;</xsl:text>

            <!-- Unidades -->
            <xsl:text>&#9;modelo_em_loja:unidades "</xsl:text>
            <xsl:value-of select="Unidades"/>
            <xsl:text>" . &#xa;</xsl:text>
          </xsl:for-each>
          <xsl:text>&#xa;&#xa;</xsl:text>
      </xsl:for-each>
  </xsl:template>

  <xsl:template match="root/Produtos/Aspirador">
      <xsl:for-each select="Modelo">
          <!-- Modelo -->
          <!-- ID -->
          <xsl:text>modelo:</xsl:text>
          <xsl:value-of select="ID"/>
          <xsl:text>&#xa;</xsl:text>

          <!-- tipo -->
          <xsl:text>&#9;a aspirador:</xsl:text>
          <xsl:text> ; &#xa;</xsl:text>

          <!-- Nome -->
          <xsl:text>&#9;modelo:nome "</xsl:text>
          <xsl:value-of select="Nome"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Marca -->
          <xsl:text>&#9;modelo:marca "</xsl:text>
          <xsl:value-of select="Marca"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Categoria -->
          <xsl:text>&#9;modelo:categoria "</xsl:text>
          <xsl:value-of select="Categoria"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- PotenciaMax -->
          <xsl:text>&#9;modelo:potenciamax "</xsl:text>
          <xsl:value-of select="PotenciaMax"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- VolumeMaxDep -->
          <xsl:text>&#9;modelo:volumemaxdep "</xsl:text>
          <xsl:value-of select="VolumeMaxDep"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Preco -->
          <xsl:text>&#9;modelo:preco "</xsl:text>
          <xsl:value-of select="Preco"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Loja -->
          <xsl:text>&#9;modelo:loja </xsl:text>
          <xsl:for-each select="Loja">
              <xsl:text>modelo_em_loja:</xsl:text>
              <xsl:value-of select="../ID"/>
              <xsl:value-of select="ID"/>
              <xsl:choose>
                  <xsl:when test="position() != last()"> , &#xa;&#9;&#9;&#9;&#9;</xsl:when>
              </xsl:choose>
          </xsl:for-each>
          <xsl:text> . &#xa;</xsl:text>

          <xsl:for-each select="Loja">
            <!-- modelo_em_loja -->
            <!-- ID -->
            <xsl:text>modelo_em_loja:</xsl:text>
            <xsl:value-of select="../ID"/>
            <xsl:value-of select="ID"/>
            <xsl:text>&#xa;</xsl:text>

            <!-- Loja ID -->
            <xsl:text>&#9;modelo_em_loja:LojaID </xsl:text>
            <xsl:text>loja:</xsl:text>
      			<xsl:value-of select="ID"/>
            <xsl:text> ; &#xa;</xsl:text>

            <!-- Unidades -->
            <xsl:text>&#9;modelo_em_loja:unidades "</xsl:text>
            <xsl:value-of select="Unidades"/>
            <xsl:text>" . &#xa;</xsl:text>
          </xsl:for-each>
          <xsl:text>&#xa;&#xa;</xsl:text>
      </xsl:for-each>
  </xsl:template>

  <xsl:template match="root/Produtos/GamingPc">
      <xsl:for-each select="Modelo">
          <!-- Modelo -->
          <!-- ID -->
          <xsl:text>modelo:</xsl:text>
          <xsl:value-of select="ID"/>
          <xsl:text>&#xa;</xsl:text>

          <!-- tipo -->
          <xsl:text>&#9;a gaming_pc:</xsl:text>
          <xsl:text> ; &#xa;</xsl:text>

          <!-- Nome -->
          <xsl:text>&#9;modelo:nome "</xsl:text>
          <xsl:value-of select="Nome"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Marca -->
          <xsl:text>&#9;modelo:marca "</xsl:text>
          <xsl:value-of select="Marca"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Categoria -->
          <xsl:text>&#9;modelo:categoria "</xsl:text>
          <xsl:value-of select="Categoria"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Ram -->
          <xsl:text>&#9;modelo:ram "</xsl:text>
    			<xsl:value-of select="Ram"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- Processador -->
          <xsl:text>&#9;modelo:processador "</xsl:text>
    			<xsl:value-of select="Processador"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- CapacidadeDisco -->
          <xsl:text>&#9;modelo:capacidadedisco "</xsl:text>
    			<xsl:value-of select="CapacidadeDisco"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- Gráfica -->
          <xsl:text>&#9;modelo:grafica "</xsl:text>
    			<xsl:value-of select="Grafica"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- TamanhoEcra -->
          <xsl:text>&#9;modelo:tamanhoecra "</xsl:text>
    			<xsl:value-of select="TamanhoEcra"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- Preco -->
          <xsl:text>&#9;modelo:preco "</xsl:text>
          <xsl:value-of select="Preco"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Loja -->
          <xsl:text>&#9;modelo:loja </xsl:text>
          <xsl:for-each select="Loja">
              <xsl:text>modelo_em_loja:</xsl:text>
              <xsl:value-of select="../ID"/>
              <xsl:value-of select="ID"/>
              <xsl:choose>
                  <xsl:when test="position() != last()"> , &#xa;&#9;&#9;&#9;&#9;</xsl:when>
              </xsl:choose>
          </xsl:for-each>
          <xsl:text> . &#xa;</xsl:text>

          <xsl:for-each select="Loja">
            <!-- modelo_em_loja -->
            <!-- ID -->
            <xsl:text>modelo_em_loja:</xsl:text>
            <xsl:value-of select="../ID"/>
            <xsl:value-of select="ID"/>
            <xsl:text>&#xa;</xsl:text>

            <!-- Loja ID -->
            <xsl:text>&#9;modelo_em_loja:LojaID </xsl:text>
            <xsl:text>loja:</xsl:text>
      			<xsl:value-of select="ID"/>
            <xsl:text> ; &#xa;</xsl:text>

            <!-- Unidades -->
            <xsl:text>&#9;modelo_em_loja:unidades "</xsl:text>
            <xsl:value-of select="Unidades"/>
            <xsl:text>" . &#xa;</xsl:text>
          </xsl:for-each>
          <xsl:text>&#xa;&#xa;</xsl:text>
      </xsl:for-each>
  </xsl:template>

  <xsl:template match="root/Produtos/Consolas">
      <xsl:for-each select="Modelo">
          <!-- Modelo -->
          <!-- ID -->
          <xsl:text>modelo:</xsl:text>
          <xsl:value-of select="ID"/>
          <xsl:text>&#xa;</xsl:text>

          <!-- tipo -->
          <xsl:text>&#9;a consola:</xsl:text>
          <xsl:text> ; &#xa;</xsl:text>

          <!-- Nome -->
          <xsl:text>&#9;modelo:nome "</xsl:text>
          <xsl:value-of select="Nome"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Marca -->
          <xsl:text>&#9;modelo:marca "</xsl:text>
          <xsl:value-of select="Marca"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Categoria -->
          <xsl:text>&#9;modelo:categoria "</xsl:text>
          <xsl:value-of select="Categoria"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- CapacidadeDisco -->
          <xsl:text>&#9;modelo:capacidadedisco "</xsl:text>
    			<xsl:value-of select="CapacidadeDisco"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- Cor -->
          <xsl:text>&#9;modelo:cor "</xsl:text>
    			<xsl:value-of select="Cor"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- JogoIncluido -->
          <xsl:text>&#9;modelo:jogoincluido "</xsl:text>
    			<xsl:value-of select="JogoIncluido"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- Preco -->
          <xsl:text>&#9;modelo:preco "</xsl:text>
          <xsl:value-of select="Preco"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Loja -->
          <xsl:text>&#9;modelo:loja </xsl:text>
          <xsl:for-each select="Loja">
              <xsl:text>modelo_em_loja:</xsl:text>
              <xsl:value-of select="../ID"/>
              <xsl:value-of select="ID"/>
              <xsl:choose>
                  <xsl:when test="position() != last()"> , &#xa;&#9;&#9;&#9;&#9;</xsl:when>
              </xsl:choose>
          </xsl:for-each>
          <xsl:text> . &#xa;</xsl:text>

          <xsl:for-each select="Loja">
            <!-- modelo_em_loja -->
            <!-- ID -->
            <xsl:text>modelo_em_loja:</xsl:text>
            <xsl:value-of select="../ID"/>
            <xsl:value-of select="ID"/>
            <xsl:text>&#xa;</xsl:text>

            <!-- Loja ID -->
            <xsl:text>&#9;modelo_em_loja:LojaID </xsl:text>
            <xsl:text>loja:</xsl:text>
      			<xsl:value-of select="ID"/>
            <xsl:text> ; &#xa;</xsl:text>

            <!-- Unidades -->
            <xsl:text>&#9;modelo_em_loja:unidades "</xsl:text>
            <xsl:value-of select="Unidades"/>
            <xsl:text>" . &#xa;</xsl:text>
          </xsl:for-each>
          <xsl:text>&#xa;&#xa;</xsl:text>
      </xsl:for-each>
  </xsl:template>

  <xsl:template match="root/Produtos/Jogos">
      <xsl:for-each select="Modelo">
          <!-- Modelo -->
          <!-- ID -->
          <xsl:text>modelo:</xsl:text>
          <xsl:value-of select="ID"/>
          <xsl:text>&#xa;</xsl:text>

          <!-- tipo -->
          <xsl:text>&#9;a jogo:</xsl:text>
          <xsl:text> ; &#xa;</xsl:text>

          <!-- Nome -->
          <xsl:text>&#9;modelo:nome "</xsl:text>
          <xsl:value-of select="Nome"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Marca -->
          <xsl:text>&#9;modelo:marca "</xsl:text>
          <xsl:value-of select="Marca"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Categoria -->
          <xsl:text>&#9;modelo:categoria "</xsl:text>
          <xsl:value-of select="Categoria"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Preco -->
          <xsl:text>&#9;modelo:preco "</xsl:text>
          <xsl:value-of select="Preco"/>
          <xsl:text>" ; &#xa;</xsl:text>

          <!-- Loja -->
          <xsl:text>&#9;modelo:loja </xsl:text>
          <xsl:for-each select="Loja">
              <xsl:text>modelo_em_loja:</xsl:text>
              <xsl:value-of select="../ID"/>
              <xsl:value-of select="ID"/>
              <xsl:choose>
                  <xsl:when test="position() != last()"> , &#xa;&#9;&#9;&#9;&#9;</xsl:when>
              </xsl:choose>
          </xsl:for-each>
          <xsl:text> . &#xa;</xsl:text>

          <xsl:for-each select="Loja">
            <!-- modelo_em_loja -->
            <!-- ID -->
            <xsl:text>modelo_em_loja:</xsl:text>
            <xsl:value-of select="../ID"/>
            <xsl:value-of select="ID"/>
            <xsl:text>&#xa;</xsl:text>

            <!-- Loja ID -->
            <xsl:text>&#9;modelo_em_loja:LojaID </xsl:text>
            <xsl:text>loja:</xsl:text>
      			<xsl:value-of select="ID"/>
            <xsl:text> ; &#xa;</xsl:text>

            <!-- Unidades -->
            <xsl:text>&#9;modelo_em_loja:unidades "</xsl:text>
            <xsl:value-of select="Unidades"/>
            <xsl:text>" . &#xa;</xsl:text>
          </xsl:for-each>
          <xsl:text>&#xa;&#xa;</xsl:text>
      </xsl:for-each>
  </xsl:template>

  <xsl:template match="root/Clientes">

      <xsl:for-each select="Cliente">
          <!-- Cliente -->
          <!-- @id -->
          <xsl:text>cliente:</xsl:text>
    			<xsl:value-of select="@id"/>
    			<xsl:text>&#xa;</xsl:text>

          <!-- tipo -->
          <xsl:text>&#9;a cliente:</xsl:text>
    			<xsl:text> ; &#xa;</xsl:text>

          <!-- @nome -->
          <xsl:text>&#9;cliente:nome "</xsl:text>
    			<xsl:value-of select="@nome"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- @datanascimento -->
          <xsl:text>&#9;cliente:datanascimento "</xsl:text>
    			<xsl:value-of select="@datanascimento"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- Morada -->
          <xsl:text>&#9;cliente:morada </xsl:text>
    			<xsl:text>morada:</xsl:text>
          <xsl:value-of select="@id"/>
          <xsl:text> ; &#xa;</xsl:text>

          <!-- Contacto -->
          <xsl:text>&#9;cliente:contacto </xsl:text>
    			<xsl:text>contacto:</xsl:text>
          <xsl:value-of select="@id"/>
          <xsl:text> ; &#xa;</xsl:text>

          <!-- WishList -->
          <xsl:text>&#9;cliente:wishlist </xsl:text>
          <xsl:for-each select="WishLists/WishList">
              <xsl:text>wishlist:</xsl:text>
              <xsl:value-of select="ancestor::Cliente/@id"/>
              <xsl:value-of select="@id"/>
              <xsl:choose>
                  <xsl:when test="position() != last()"> , &#xa;&#9;&#9;&#9;&#9;</xsl:when>
              </xsl:choose>
          </xsl:for-each>
          <xsl:text> ; &#xa;</xsl:text>

          <!-- Cart -->
          <xsl:text>&#9;cliente:cart </xsl:text>
          <xsl:for-each select="Cart/Modelo">
                <xsl:text>modelo:</xsl:text>
                <xsl:value-of select="@id"/>
                <xsl:choose>
                    <xsl:when test="position() != last()"> , &#xa;&#9;&#9;&#9;&#9;</xsl:when>
                </xsl:choose>
          </xsl:for-each>
          <xsl:text> ; &#xa;</xsl:text>

          <!-- Visited -->
          <xsl:text>&#9;cliente:visited </xsl:text>
          <xsl:for-each select="Visited/Modelo">
              <xsl:text>visited:</xsl:text>
              <xsl:value-of select="ancestor::Cliente/@id"/>
              <xsl:value-of select="@id"/>
              <xsl:choose>
                  <xsl:when test="position() != last()"> , &#xa;&#9;&#9;&#9;&#9;</xsl:when>
              </xsl:choose>
          </xsl:for-each>
          <xsl:text> . &#xa;</xsl:text>

          <!-- Morada -->
          <!-- @id -->
          <xsl:text>morada:</xsl:text>
    			<xsl:value-of select="@id"/>
    			<xsl:text>&#xa;</xsl:text>

          <!-- tipo -->
          <xsl:text>&#9;a morada:</xsl:text>
    			<xsl:text> ; &#xa;</xsl:text>

          <!-- @rua -->
          <xsl:text>&#9;morada:rua "</xsl:text>
    			<xsl:value-of select="Morada/@rua"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- @codigopostal -->
          <xsl:text>&#9;morada:codigopostal "</xsl:text>
    			<xsl:value-of select="Morada/@codigopostal"/>
          <xsl:text>" . &#xa;</xsl:text>

          <!-- Contacto -->
          <!-- @id -->
          <xsl:text>contacto:</xsl:text>
    			<xsl:value-of select="@id"/>
    			<xsl:text>&#xa;</xsl:text>

          <!-- tipo -->
          <xsl:text>&#9;a contacto:</xsl:text>
    			<xsl:text> ; &#xa;</xsl:text>

          <!-- @telefone -->
          <xsl:text>&#9;contacto:telefone "</xsl:text>
    			<xsl:value-of select="Contacto/@telefone"/>
    			<xsl:text>" ; &#xa;</xsl:text>

          <!-- @email -->
          <xsl:text>&#9;contacto:email "</xsl:text>
    			<xsl:value-of select="Contacto/@email"/>
          <xsl:text>" . &#xa;</xsl:text>

          <xsl:for-each select="WishLists/WishList">
            <!-- WishList -->
            <!-- @id -->
            <xsl:text>wishlist:</xsl:text>
            <xsl:value-of select="ancestor::Cliente/@id"/>
            <xsl:value-of select="@id"/>
      			<xsl:text>&#xa;</xsl:text>

            <!-- tipo -->
            <xsl:text>&#9;a wishlist:</xsl:text>
      			<xsl:text> ; &#xa;</xsl:text>

            <!-- @nome -->
            <xsl:text>&#9;wishlist:nome "</xsl:text>
      			<xsl:value-of select="@nome"/>
            <xsl:text>" ; &#xa;</xsl:text>

            <!-- @modelo -->
            <xsl:text>&#9;wishlist:modelo </xsl:text>
            <xsl:for-each select="Modelo">
                <xsl:text>modelo:</xsl:text>
                <xsl:value-of select="@id"/>
                <xsl:choose>
                    <xsl:when test="position() != last()"> , &#xa;&#9;&#9;&#9;&#9;</xsl:when>
                </xsl:choose>
            </xsl:for-each>
            <xsl:text> . &#xa;</xsl:text>
          </xsl:for-each>

          <xsl:for-each select="Visited/Modelo">
            <!-- Visited -->
            <!-- @id -->
            <xsl:text>visited:</xsl:text>
            <xsl:value-of select="ancestor::Cliente/@id"/>
            <xsl:value-of select="@id"/>
      			<xsl:text>&#xa;</xsl:text>

            <!-- tipo -->
            <xsl:text>&#9;a visited:</xsl:text>
      			<xsl:text> ; &#xa;</xsl:text>

            <!-- @modelo -->
            <xsl:text>&#9;visited:modelo </xsl:text>
            <xsl:text>&#9;modelo:</xsl:text>
      			<xsl:value-of select="@id"/>
            <xsl:text> ; &#xa;</xsl:text>

            <!-- @times -->
            <xsl:text>&#9;visited:times "</xsl:text>
      			<xsl:value-of select="@times"/>
            <xsl:text>" ; &#xa;</xsl:text>

            <!-- @last_visit -->
            <xsl:text>&#9;visited:last_visit "</xsl:text>
      			<xsl:value-of select="@last_visit"/>
            <xsl:text>" . &#xa;</xsl:text>
          </xsl:for-each>

          <xsl:text>&#xa;&#xa;</xsl:text>
      </xsl:for-each>

  </xsl:template>


</xsl:stylesheet>
