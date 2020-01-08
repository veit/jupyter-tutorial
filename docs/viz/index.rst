Datenvisualisierung
===================

.. graphviz::
   :layout: neato

    graph python_visualisation_landscape {
        graph [fontname = "Calibri", fontsize="16", overlap=false];
        node [fontname = "Calibri", fontsize="16", style="bold"];
        edge [fontname = "Calibri", fontsize="16", style="bold"];
        tooltip="Python Visualisation Landscape";

        // OpenGL
        opengl [
            label="OpenGL",
            tooltip="Open Graphics Library",
            color="mediumpurple",
            target="_top",
            href="../viz/opengl/index.html"]
        vispy [
            label="Vispy",
            tooltip="Python-Bibliothek für\ninteraktive wissenschaftliche\nVisualisierungen",
            color="mediumpurple",
            target="_top",
            href="http://vispy.org/"]
        glumpy [
            label="Glumpy",
            tooltip="Schnittstelle zwischen\nnumpy und OpenGL",
            color="mediumpurple",
            target="_top",
            href="https://glumpy.github.io/"]
        opengl -- vispy [color="mediumpurple"]
        opengl -- glumpy [color="mediumpurple"]

        // Matplotlib
        mpl [
            label="Matplotlib",
            tooltip="Python-Bibliothek\nfür 2D-Plots",
            color="slateblue"
            target="_top",
            href="../viz/matplotlib/index.html"]
        pandas [
            label="Pandas",
            tooltip="Pandas Datenstrukturen mit\nMatplotlib visualisieren",
            color="slateblue",
            target="_top",
            href="../viz/matplotlib/pandas.html"]
        geopandas [
            label="GeoPandas",
            tooltip="geopandas erweitert Pandas um geometrische Datentypen",
            color="slateblue",
            target="_top",
            href="../viz/matplotlib/geopandas.html"]
        seaborn [
            label="Seaborn",
            tooltip="High-level-Datenvisualisierung\nbasierend auf Matplotlib",
            color="slateblue",
            target="_top",
            href="../viz/matplotlib/seaborn.html"]
        ggpy [
            label="ggpy",
            tooltip="ggplot-Port für Python",
            color="slateblue",
            target="_top",
            href="https://github.com/yhat/ggpy"]
        scikit_plot [
            label="Scikit-plot",
            tooltip="Plotting-Bibliothek für\nScikit-learn-Objekte",
            color="slateblue",
            target="_top",
            href="https://scikit-plot.readthedocs.io/"]
        yellow_brick [
            label="Yellow brick",
            tooltip="Tools für die visuelle Analyse und Diagnose\nvon Scikit-learn-Projekten",
            color="slateblue",
            target="_top",
            href="https://www.scikit-yb.org/"]
        networkx [
            label="NetworkX",
            tooltip="Erstellen, Ändern und Analysieren\nkomplexer Netzwerke",
            color="slateblue",
            target="_top",
            href="../viz/matplotlib/networkx.html"]
        graphviz [
            label="Graphviz",
            tooltip="Mächtige Visualisierungssoftware\nfür Graphen",
            color="gray",
            target="_top",
            href="../viz/matplotlib/graphviz.html"]
        cartopy [
            label="Cartopy",
            tooltip="Erstellen von Karten und\nAnalyse von Geodaten",
            color="slateblue",
            target="_top",
            href="../viz/matplotlib/cartopy.html"]
        iris [
            label="Iris",
            tooltip="Visualisierung auf Basis der Climate\nand Forecast (CF) Conventions",
            color="slateblue",
            target="_top",
            href="../viz/matplotlib/iris.html"]
        mpl -- pandas [color="slateblue"]
        pandas  -- geopandas [color="slateblue"]
        mpl -- seaborn [color="slateblue"]
        mpl -- ggpy [color="slateblue"]
        mpl -- scikit_plot [color="slateblue"]
        mpl -- yellow_brick [color="slateblue"]
        networkx -- graphviz [color="slateblue;0.5:gray"]
        mpl -- networkx [color="slateblue"]
        mpl -- cartopy [color="slateblue"]
        iris -- mpl [color="slateblue"]
        iris -- cartopy [color="slateblue"]
        mpl -- mpld3 [color="slateblue;0.5:deepskyblue"]
        mpl -- mpl_altair [color="slateblue;0.5:darkturquoise"]

        // Bokeh
        bokeh [
            label="Bokeh",
            tooltip="Interaktive Python-Bibliothek\nzur Datenvisualisierung\nin modernen Webbrowsern",
            color="royalblue",
            target="_top",
            href="../viz/bokeh/index.html"]
        vaex [
            label="Vaex",
            tooltip="Python-Bibliothek zur Datenanalyse\nund -visualisierung",
            color="royalblue",
            target="_top",
            href="https://github.com/vaexio/vaex"]
        holoviews [
            label="HoloViews",
            tooltip="Python-Bibliothek zur Datenanalyse\nund -visualisierung",
            color="royalblue",
            target="_top",
            href="http://holoviews.org/"]
        datashader [
            label="Datashader",
            tooltip="Grafik-Pipeline-System für\naussagekräftige Darstellungen\ngroßer Datensätze",
            color="royalblue",
            target="_top",
            href="../viz/bokeh/integration/datashader.html"]
        vaex -- bokeh [color="royalblue;0.5:royalblue"]
        holoviews -- bokeh [color="royalblue;0.5:royalblue"]
        datashader -- bokeh [color="royalblue;0.5:royalblue"]
        datashader -- holoviews [color="royalblue"]
        vaex -- mpl [color="royalblue;0.5:slateblue"]
        vaex -- bqplot [color="royalblue;0.5:deepskyblue"]
        vaex -- opengl [color="royalblue;0.5:mediumpurple"]
        holoviews -- mpl [color="royalblue;0.5:slateblue"]
        datashader -- mpl [color="royalblue;0.5:slateblue"]

        // D3.js
        d3js [
            label="D3.js",
            tooltip="Javascript-Bibliothek mit mächtigen\nVisualisierungskomponenten",
            color="deepskyblue",
            target="_top",
            href="../viz/d3js/index.html"]
        bqplot [
            label="bqplot",
            tooltip="Interaktive Plots\nmit D3.js und ipywidgets",
            color="deepskyblue",
            target="_top",
            href="../viz/d3js/bqplot/index.html"]
        d3po [
            label="d3po",
            tooltip="Javascript-Bibliothekt zum\nErstellen von D3.js-Charts",
            color="deepskyblue",
            target="_top",
            href="https://github.com/adamlabadorf/d3po"]
        mpld3 [
            label="mpld3",
            tooltip="Matplotlib für\nden Webbrowser",
            color="deepskyblue",
            target="_top",
            href="https://mpld3.github.io/"]
        d3js -- bqplot [color="deepskyblue"]
        d3js -- mpld3 [color="deepskyblue"]
        d3js -- d3po [color="deepskyblue"]
        d3js -- vega [color="deepskyblue;0.5:darkturquoise"]
        d3js -- javascript [color="deepskyblue;0.5:cyan"]

        // Vega
        vega [
            label="Vega",
            tooltip="Deklarative Sprache für\ninteraktive Visualisierungen",
            color="darkturquoise",
            target="_top",
            href="../viz/vega/index.html"]
        vincent [
            label="Vincent",
            tooltip="Python-Bibliothek für\nVega-Anwendungen",
            color="darkturquoise",
            target="_top",
            href="https://vincent.readthedocs.io/"]
        vega_light [
            label="Vega-Lite",
            tooltip="High-level-Grammatik für\nkomplexe Vega-Anwendungen",
            color="darkturquoise",
            target="_top",
            href="https://bqplot.readthedocs.io/"]
        altair [
            label="Altair",
            tooltip="Deklarative Visualisierung\nin Python",
            color="darkturquoise",
            target="_top",
            href="https://altair-viz.github.io/"]
        mpl_altair [
            label="Matplotlib Altair",
            tooltip="Matplotlib-Renderer\nfür Altair",
            color="darkturquoise",
            target="_top",
            href="https://matplotlib.org/mpl-altair/"]
        vega -- vincent [color="darkturquoise"]
        vega -- vega_light [color="darkturquoise"]
        vega_light -- altair [color="darkturquoise"]
        altair -- mpl_altair [color="darkturquoise"]

        // Javascript
        javascript [
            label="Javascript",
            tooltip="Skriptsprache, die ursprünglich für\ndynamisches HTML in Webbrowsern\nentwickelt wurde",
            color="cyan",
            target="_top",
            href="../viz/js/index.html"]
        plotly [
            label="plotly",
            tooltip="Interaktive Graphikbibliothek\nfür Python",
            color="cyan",
            target="_top",
            href="https://github.com/plotly/plotly.py"]
        cufflinks [
            label="Cufflinks",
            tooltip="Interaktive Plotly-Plots\nfür Pandas",
            color="cyan",
            target="_top",
            href="https://github.com/santosjorge/cufflinks"]
        pythreejs [
            label="pythreejs",
            tooltip="Notebook-Extension\nfür WebGL-fähige Webbrowser",
            color="cyan",
            target="_top",
            href="../viz/js/pythreejs.html"]
        ipyvolume [
            label="IPyvolume",
            tooltip="Python-Bibliothek zur\nVisualisierung von\nVolumen und -Glyphen",
            color="cyan",
            target="_top",
            href="../viz/js/ipyvolume.html"]
        toyplot [
            label="Toyplot",
            tooltip="Leichtgewichtige Bibliothek\nfür ästhetische Plots",
            color="cyan",
            target="_top",
            href="https://toyplot.readthedocs.io/"]
        ipyleaflet [
            label="ipyleaflet",
            tooltip="Interaktive Karten für\nJupyter Notebooks",
            color="cyan",
            target="_top",
            href="../viz/js/ipyleaflet.html"]
        javascript -- ipyvolume [color="cyan"]
        javascript -- plotly [color="cyan"]
        plotly -- cufflinks [color="cyan"]
        javascript -- ipyleaflet [color="cyan"]
        javascript -- toyplot [color="cyan"]
        javascript -- bokeh [color="cyan;0.5:royalblue"]
        javascript -- pythreejs [color="cyan"]
    }

.. toctree::
    :titlesonly:
    :maxdepth: 0
    :hidden:

    matplotlib/index
    vega/index
    bokeh/index
    opengl/index
    d3js/index
    js/index

