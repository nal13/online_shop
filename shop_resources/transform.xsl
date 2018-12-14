<?xml version="1.0" encoding="utf-8"?>

<!DOCTYPE rdf:RDF[
  <!ENTITY rdf 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'>
  <!ENTITY ns "http://www.iro.umontreal.ca/lapalme/ns#">
]>

<xsl:stylesheet version="2.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:html="http://www.w3.org/1999/xhtml"
  xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
  xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  xmlns:xs="http://www.w3.org/TR/2008/REC-xml-20081126#"
  xmlns:foaf="http://xmlns.com/foaf/0.1/"
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
    <xsl:text disable-output-escaping="yes">@prefix Computador: &lt;http://www.shop.pt/computador/&gt; . &#xa;</xsl:text>
    <xsl:text disable-output-escaping="yes">@prefix Telemovel: &lt;http://www.shop.pt/telemovel/&gt; . &#xa;</xsl:text>
    <xsl:text disable-output-escaping="yes">@prefix Tablet: &lt;http://www.shop.pt/tablet/&gt; . &#xa;</xsl:text>
    <xsl:text disable-output-escaping="yes">@prefix Camara: &lt;http://www.shop.pt/camara/&gt; . &#xa;</xsl:text>
    <xsl:text disable-output-escaping="yes">@prefix Drone: &lt;http://www.shop.pt/drone/&gt; . &#xa;</xsl:text>
    <xsl:text disable-output-escaping="yes">@prefix Tv: &lt;http://www.shop.pt/tv/&gt; . &#xa;</xsl:text>
    <xsl:text disable-output-escaping="yes">@prefix LeitorBlueray: &lt;http://www.shop.pt/leitorblueray/&gt; . &#xa;</xsl:text>
    <xsl:text disable-output-escaping="yes">@prefix MaquinaCafe: &lt;http://www.shop.pt/maquinacafe/&gt; . &#xa;</xsl:text>
    <xsl:text disable-output-escaping="yes">@prefix Microondas: &lt;http://www.shop.pt/microondas/&gt; . &#xa;</xsl:text>
    <xsl:text disable-output-escaping="yes">@prefix MaquinaLavarRoupa: &lt;http://www.shop.pt/maquinalavarroupa/&gt; . &#xa;</xsl:text>
    <xsl:text disable-output-escaping="yes">@prefix MaquinaSecarRoupa: &lt;http://www.shop.pt/maquinasecarroupa/&gt; . &#xa;</xsl:text>
    <xsl:text disable-output-escaping="yes">@prefix Aspirador: &lt;http://www.shop.pt/aspirador/&gt; . &#xa;</xsl:text>
    <xsl:text disable-output-escaping="yes">@prefix GamingPc: &lt;http://www.shop.pt/gamingpc/&gt; . &#xa;</xsl:text>
    <xsl:text disable-output-escaping="yes">@prefix Consola: &lt;http://www.shop.pt/consola/&gt; . &#xa;</xsl:text>
    <xsl:text disable-output-escaping="yes">@prefix Jogo: &lt;http://www.shop.pt/jogo/&gt; . &#xa;</xsl:text>
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
          <xsl:text>&#9;a Computador:</xsl:text>
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
          <xsl:text>&#9;a Telemovel:</xsl:text>
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
          <xsl:text>&#9;a Tablet:</xsl:text>
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
          <xsl:text>&#9;a Camara:</xsl:text>
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
          <xsl:text>&#9;a Drone:</xsl:text>
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
          <xsl:text>&#9;a Tv:</xsl:text>
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
          <xsl:text>&#9;a LeitorBlueray:</xsl:text>
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
          <xsl:text>&#9;a MaquinaCafe:</xsl:text>
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
          <xsl:text>&#9;a Microondas:</xsl:text>
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
          <xsl:text>&#9;a MaquinaLavarRoupa:</xsl:text>
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
          <xsl:text>&#9;a MaquinaSecarRoupa:</xsl:text>
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
          <xsl:text>&#9;a Aspirador:</xsl:text>
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
          <xsl:text>&#9;a GamingPc:</xsl:text>
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
          <xsl:text>&#9;a Consola:</xsl:text>
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
          <xsl:text>&#9;a Jogo:</xsl:text>
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


</xsl:stylesheet>
