Überblick über die Bibliotheken zur Datenvisualisierung
=======================================================

Technologien
------------

.. graphviz::
   :layout: neato

    graph python_visualisation_landscape {
        graph [fontname = "Calibri", fontsize="16", overlap=false];
        node [fontname = "Calibri", fontsize="16", style="bold", penwidth="5px"];
        edge [fontname = "Calibri", fontsize="16", style="bold", penwidth="5px"];
        tooltip="Python Visualisation Landscape";

        // OpenGL
        opengl [
            label="OpenGL",
            tooltip="Open Graphics Library",
            color="#FF66B3",
            target="_top",
            href="../viz/opengl/index.html"]
        vispy [
            label="Vispy",
            tooltip="Python-Bibliothek für\ninteraktive wissenschaftliche\nVisualisierungen",
            color="#FF66B3",
            target="_top",
            href="http://vispy.org/"]
        glumpy [
            label="Glumpy",
            tooltip="Schnittstelle zwischen\nnumpy und OpenGL",
            color="#FF66B3",
            target="_top",
            href="https://glumpy.github.io/"]
        opengl -- vispy [color="#FF66B3"]
        opengl -- glumpy [color="#FF66B3"]

        // Matplotlib
        mpl [
            label="Matplotlib",
            tooltip="Python-Bibliothek\nfür 2D-Plots",
            color="#BF80FF"
            target="_top",
            href="../viz/matplotlib/index.html"]
        pandas [
            label="Pandas",
            tooltip="Pandas Datenstrukturen mit\nMatplotlib visualisieren",
            color="#BF80FF",
            target="_top",
            href="../viz/matplotlib/pandas/index.html"]
        geopandas [
            label="GeoPandas",
            tooltip="geopandas erweitert Pandas um geometrische Datentypen",
            color="#BF80FF",
            target="_top",
            href="../viz/matplotlib/geopandas/index.html"]
        seaborn [
            label="seaborn",
            tooltip="High-level-Datenvisualisierung\nbasierend auf Matplotlib",
            color="#BF80FF",
            target="_top",
            href="../viz/matplotlib/seaborn/index.html"]
        ggpy [
            label="ggpy",
            tooltip="ggplot-Port für Python",
            color="#BF80FF",
            target="_top",
            href="https://github.com/yhat/ggpy"]
        plotnine [
            label="plotnine",
            tooltip="Python-Implementierung von ggplot2",
            color="#BF80FF",
            target="_top",
            href="../viz/matplotlib/plotnine/index.html"]
        scikit_plot [
            label="Scikit-plot",
            tooltip="Plotting-Bibliothek für\nScikit-learn-Objekte",
            color="#BF80FF",
            target="_top",
            href="https://scikit-plot.readthedocs.io/"]
        yellowbrick [
            label="Yellowbrick",
            tooltip="Tools für die visuelle Analyse und Diagnose\nvon Scikit-learn-Projekten",
            color="#BF80FF",
            target="_top",
            href="https://www.scikit-yb.org/"]
        networkx [
            label="NetworkX",
            tooltip="Erstellen, Ändern und Analysieren\nkomplexer Netzwerke",
            color="#BF80FF",
            target="_top",
            href="../viz/matplotlib/networkx.html"]
        graphviz [
            label="Graphviz",
            tooltip="Mächtige Visualisierungssoftware\nfür Graphen",
            color="#cccccc",
            target="_top",
            href="../viz/matplotlib/graphviz.html"]
        cartopy [
            label="Cartopy",
            tooltip="Erstellen von Karten und\nAnalyse von Geodaten",
            color="#BF80FF",
            target="_top",
            href="../viz/matplotlib/cartopy/index.html"]
        iris [
            label="Iris",
            tooltip="Visualisierung auf Basis der Climate\nand Forecast (CF) Conventions",
            color="#BF80FF",
            target="_top",
            href="../viz/matplotlib/iris.html"]
        yt [
            label="yt",
            tooltip="Python-Bibliothek zur Analyse\nund Visualisierung von Volumendaten",
            color="#BF80FF",
            target="_top",
            href="../viz/matplotlib/yt.html"]
        mpl -- pandas [color="#BF80FF"]
        pandas  -- geopandas [color="#BF80FF"]
        mpl -- seaborn [color="#BF80FF"]
        mpl -- ggpy [color="#BF80FF"]
        mpl -- plotnine [color="#BF80FF"]
        mpl -- scikit_plot [color="#BF80FF"]
        mpl -- yellowbrick [color="#BF80FF"]
        networkx -- graphviz [color="#BF80FF;0.5:#cccccc"]
        mpl -- networkx [color="#BF80FF"]
        mpl -- cartopy [color="#BF80FF"]
        iris -- mpl [color="#BF80FF"]
        iris -- cartopy [color="#BF80FF"]
        yt -- mpl [color="#BF80FF"]
        yt -- opengl [color="#BF80FF;0.5:#FF66B3", style="dashed"]
        mpl -- mpld3 [color="#BF80FF;0.5:#4da6ff"]
        mpl -- ipympl [color="#BF80FF;0.5:#00FFFF"]
        mpl -- mpl_altair [color="#BF80FF;0.5:#00FF80"]

        // Bokeh
        bokeh [
            label="Bokeh",
            tooltip="Interaktive Python-Bibliothek\nzur Datenvisualisierung\nin modernen Webbrowsern",
            color="#9999FF",
            target="_top",
            href="../viz/bokeh/index.html"]
        vaex [
            label="Vaex",
            tooltip="Python-Bibliothek zur Datenanalyse\nund -visualisierung",
            color="#9999FF",
            target="_top",
            href="https://github.com/vaexio/vaex"]
        holoviews [
            label="HoloViews",
            tooltip="Python-Bibliothek zur Datenanalyse\nund -visualisierung",
            color="#9999FF",
            target="_top",
            href="http://holoviews.org/"]
        hvplot [
            label="hvPlot",
            tooltip="High-level-Plot-API\nauf Basis von HoloViews",
            color="#9999FF",
            target="_top",
            href="../viz/bokeh/integration/holoviews/hvplot/index.html"]
        datashader [
            label="Datashader",
            tooltip="Grafik-Pipeline-System für\naussagekräftige Darstellungen\ngroßer Datensätze",
            color="#9999FF",
            target="_top",
            href="../viz/bokeh/integration/datashader.html"]
        vaex -- bokeh [color="#9999FF"]
        holoviews -- bokeh [color="#9999FF"]
        holoviews -- hvplot [color="#9999FF"]
        hvplot -- pandas [color="#9999FF;0.5:#BF80FF"]
        hvplot -- geopandas [color="#9999FF;0.5:#BF80FF"]
        hvplot -- networkx [color="#9999FF;0.5:#BF80FF"]
        datashader -- bokeh [color="#9999FF"]
        networkx -- bokeh [color="#BF80FF;0.5:#9999FF"]
        datashader -- holoviews [color="#9999FF"]
        vaex -- mpl [color="#9999FF;0.5:#BF80FF"]
        vaex -- bqplot [color="#9999FF;0.5:#4da6ff"]
        vaex -- opengl [color="#9999FF;0.5:#FF66B3"]
        holoviews -- mpl [color="#9999FF;0.5:#BF80FF"]
        datashader -- mpl [color="#9999FF;0.5:#BF80FF"]

        // Vega
        vega [
            label="Vega",
            tooltip="Deklarative Sprache für\ninteraktive Visualisierungen",
            color="#00FF80",
            target="_top",
            href="../viz/vega/index.html"]
        vincent [
            label="Vincent",
            tooltip="Python-Bibliothek für\nVega-Anwendungen",
            color="#00FF80",
            target="_top",
            href="https://vincent.readthedocs.io/"]
        vega_light [
            label="Vega-Lite",
            tooltip="High-level-Grammatik für\nkomplexe Vega-Anwendungen",
            color="#00FF80",
            target="_top",
            href="https://github.com/vega/vega-lite"]
        pdvega [
            label="PdVega",
            tooltip="Interaktive Vega-Light-Plots\naus Pandas Dataframes",
            color="#00FF80",
            target="_top",
            href="../viz/vega/pdvega/index.html"]
        altair [
            label="Altair",
            tooltip="Deklarative Visualisierung\nin Python",
            color="#00FF80",
            target="_top",
            href="https://altair-viz.github.io/"]
        mpl_altair [
            label="Matplotlib Altair",
            tooltip="Matplotlib-Renderer\nfür Altair",
            color="#00FF80",
            target="_top",
            href="https://matplotlib.org/mpl-altair/"]
        vega -- vincent [color="#00FF80"]
        vega -- vega_light [color="#00FF80"]
        vega_light -- altair [color="#00FF80"]
        vega_light -- pdvega [color="#00FF80"]
        pdvega -- pandas [color="#00FF80;0.5:#BF80FF"]
        altair -- mpl_altair [color="#00FF80"]

        // D3.js
        d3js [
            label="D3.js",
            tooltip="Javascript-Bibliothek mit mächtigen\nVisualisierungskomponenten",
            color="#4da6ff",
            target="_top",
            href="../viz/d3js/index.html"]
        bqplot [
            label="bqplot",
            tooltip="Interaktive Plots\nmit D3.js und ipywidgets",
            color="#4da6ff",
            target="_top",
            href="../viz/d3js/bqplot/index.html"]
        d3po [
            label="d3po",
            tooltip="Javascript-Bibliothekt zum\nErstellen von D3.js-Charts",
            color="#4da6ff",
            target="_top",
            href="https://github.com/adamlabadorf/d3po"]
        plotly [
            label="plotly",
            tooltip="Interaktive Graphikbibliothek\nfür Python",
            color="#4da6ff",
            target="_top",
            href="https://github.com/plotly/plotly.py"]
        cufflinks [
            label="Cufflinks",
            tooltip="Interaktive Plotly-Plots\nfür Pandas",
            color="#4da6ff",
            target="_top",
            href="https://plot.ly/python/v3/ipython-notebooks/cufflinks/"]
        mpld3 [
            label="mpld3",
            tooltip="Matplotlib für\nden Webbrowser",
            color="#4da6ff",
            target="_top",
            href="https://mpld3.github.io/"]
        d3js -- bqplot [color="#4da6ff"]
        d3js -- mpld3 [color="#4da6ff"]
        d3js -- plotly [color="#4da6ff"]
        plotly -- cufflinks [color="#4da6ff"]
        cufflinks -- pandas [color="#4da6ff;0.5:#BF80FF"]
        d3js -- d3po [color="#4da6ff"]
        d3js -- vega [color="#4da6ff;0.5:#00FF80"]
        d3js -- javascript [color="#4da6ff;0.5:#00FFFF"]

        // Javascript
        javascript [
            label="Javascript",
            tooltip="Skriptsprache, die ursprünglich für\ndynamisches HTML in Webbrowsern\nentwickelt wurde",
            color="#00FFFF",
            target="_top",
            href="../viz/js/index.html"]
        pythreejs [
            label="pythreejs",
            tooltip="Notebook-Extension\nfür WebGL-fähige Webbrowser",
            color="#00FFFF",
            target="_top",
            href="../viz/js/pythreejs.html"]
        ipyvolume [
            label="IPyvolume",
            tooltip="Python-Bibliothek zur\nVisualisierung von\nVolumen und -Glyphen",
            color="#00FFFF",
            target="_top",
            href="../viz/js/ipyvolume.html"]
        toyplot [
            label="Toyplot",
            tooltip="Leichtgewichtige Bibliothek\nfür ästhetische Plots",
            color="#00FFFF",
            target="_top",
            href="https://toyplot.readthedocs.io/"]
        ipyleaflet [
            label="ipyleaflet",
            tooltip="Interaktive Karten für\nJupyter Notebooks",
            color="#00FFFF",
            target="_top",
            href="../viz/js/ipyleaflet.html"]
        ipympl [
            label="ipympl",
            tooltip="Matplotlib\nJupyter Extension",
            color="#00FFFF",
            target="_top",
            href="../workspace/jupyter/ipywidgets/libs/ipympl.html"]
        javascript -- ipyvolume [color="#00FFFF"]
        javascript -- ipyleaflet [color="#00FFFF"]
        javascript -- ipympl [color="#00FFFF"]
        javascript -- toyplot [color="#00FFFF"]
        javascript -- bokeh [color="#00FFFF;0.5:#9999FF"]
        javascript -- pythreejs [color="#00FFFF"]
    }

Aktivitäten und Lizenzen
------------------------

Mit diesem tabellarischen Überblick könnt ihr schnell die Aktivitäten und
Lizenzen der verschiedenen Bibliotheken vergleichen. So könnt ihr z.B. sofort
sehen, dass die Bibliotheken ggpy, scikit-plot, d3po, vincent und Matplotlib
Altair seit mindestens einem Jahr nicht mehr weiterentwickelt wurden (Stand:
13.01.2020).

.. csv-table:: GitHub-Insights
    :header: "Name", "Stars", "Mitwirkende", "Commit-Aktivität", "Lizenz"

    "`vispy <https://github.com/vispy/vispy>`_",".. image:: https://raster.shields.io/github/stars/vispy/vispy",".. image:: https://raster.shields.io/github/contributors/vispy/vispy",".. image:: https://raster.shields.io/github/commit-activity/y/vispy/vispy",".. image:: https://raster.shields.io/github/license/vispy/vispy"
    "`glumpy <https://github.com/glumpy/glumpy>`_",".. image:: https://raster.shields.io/github/stars/glumpy/glumpy",".. image:: https://raster.shields.io/github/contributors/glumpy/glumpy",".. image:: https://raster.shields.io/github/commit-activity/y/glumpy/glumpy",".. image:: https://raster.shields.io/github/license/glumpy/glumpy"
    "`Matplotlib <https://github.com/matplotlib/matplotlib>`_",".. image:: https://raster.shields.io/github/stars/matplotlib/matplotlib",".. image:: https://raster.shields.io/github/contributors/matplotlib/matplotlib",".. image:: https://raster.shields.io/github/commit-activity/y/matplotlib/matplotlib",".. image:: https://raster.shields.io/github/license/matplotlib/matplotlib"
    "`pandas <https://github.com/pandas-dev/pandas>`_",".. image:: https://raster.shields.io/github/stars/pandas-dev/pandas",".. image:: https://raster.shields.io/github/contributors/pandas-dev/pandas",".. image:: https://raster.shields.io/github/commit-activity/y/pandas-dev/pandas",".. image:: https://raster.shields.io/github/license/pandas-dev/pandas"
    "`geopandas <https://github.com/geopandas/geopandas>`_",".. image:: https://raster.shields.io/github/stars/geopandas/geopandas",".. image:: https://raster.shields.io/github/contributors/geopandas/geopandas",".. image:: https://raster.shields.io/github/commit-activity/y/geopandas/geopandas",".. image:: https://raster.shields.io/github/license/geopandas/geopandas"
    "`seaborn <https://github.com/mwaskom/seaborn>`_",".. image:: https://raster.shields.io/github/stars/mwaskom/seaborn",".. image:: https://raster.shields.io/github/contributors/mwaskom/seaborn",".. image:: https://raster.shields.io/github/commit-activity/y/mwaskom/seaborn",".. image:: https://raster.shields.io/github/license/mwaskom/seaborn"
    "`ggpy <https://github.com/yhat/ggpy>`_",".. image:: https://raster.shields.io/github/stars/yhat/ggpy",".. image:: https://raster.shields.io/github/contributors/yhat/ggpy",".. image:: https://raster.shields.io/github/commit-activity/y/yhat/ggpy",".. image:: https://raster.shields.io/github/license/yhat/ggpy"
    "`plotnine <https://github.com/has2k1/plotnine>`_",".. image:: https://raster.shields.io/github/stars/has2k1/plotnine",".. image:: https://raster.shields.io/github/contributors/has2k1/plotnine",".. image:: https://raster.shields.io/github/commit-activity/y/has2k1/plotnine",".. image:: https://raster.shields.io/github/license/has2k1/plotnine"
    "`scikit-plot <https://github.com/reiinakano/scikit-plot>`_",".. image:: https://raster.shields.io/github/stars/reiinakano/scikit-plot",".. image:: https://raster.shields.io/github/contributors/reiinakano/scikit-plot",".. image:: https://raster.shields.io/github/commit-activity/y/reiinakano/scikit-plot",".. image:: https://raster.shields.io/github/license/reiinakano/scikit-plot"
    "`Yellowbrick <https://github.com/DistrictDataLabs/yellowbrick/>`_",".. image:: https://raster.shields.io/github/stars/DistrictDataLabs/yellowbrick",".. image:: https://raster.shields.io/github/contributors/DistrictDataLabs/yellowbrick",".. image:: https://raster.shields.io/github/commit-activity/y/DistrictDataLabs/yellowbrick",".. image:: https://raster.shields.io/github/license/DistrictDataLabs/yellowbrick"
    "`networkx <https://github.com/networkx/networkx>`_",".. image:: https://raster.shields.io/github/stars/networkx/networkx",".. image:: https://raster.shields.io/github/contributors/networkx/networkx",".. image:: https://raster.shields.io/github/commit-activity/y/networkx/networkx",".. image:: https://raster.shields.io/github/license/networkx/networkx"
    "`graphviz <https://github.com/xflr6/graphviz>`_",".. image:: https://raster.shields.io/github/stars/xflr6/graphviz",".. image:: https://raster.shields.io/github/contributors/xflr6/graphviz",".. image:: https://raster.shields.io/github/commit-activity/y/xflr6/graphviz",".. image:: https://raster.shields.io/github/license/xflr6/graphviz"
    "`cartopy <https://github.com/SciTools/cartopy>`_",".. image:: https://raster.shields.io/github/stars/SciTools/cartopy",".. image:: https://raster.shields.io/github/contributors/SciTools/cartopy",".. image:: https://raster.shields.io/github/commit-activity/y/SciTools/cartopy",".. image:: https://raster.shields.io/github/license/SciTools/cartopy"
    "`iris <https://github.com/SciTools/iris>`_",".. image:: https://raster.shields.io/github/stars/SciTools/iris",".. image:: https://raster.shields.io/github/contributors/SciTools/iris",".. image:: https://raster.shields.io/github/commit-activity/y/SciTools/iris",".. image:: https://raster.shields.io/github/license/SciTools/iris"
    "`yt <https://github.com/yt-project/yt>`_",".. image:: https://raster.shields.io/github/stars/yt-project/yt",".. image:: https://raster.shields.io/github/contributors/yt-project/yt",".. image:: https://raster.shields.io/github/commit-activity/y/yt-project/yt",".. image:: https://raster.shields.io/github/license/yt-project/yt"
    "`bokeh <https://github.com/bokeh/bokeh>`_",".. image:: https://raster.shields.io/github/stars/bokeh/bokeh",".. image:: https://raster.shields.io/github/contributors/bokeh/bokeh",".. image:: https://raster.shields.io/github/commit-activity/y/bokeh/bokeh",".. image:: https://raster.shields.io/github/license/bokeh/bokeh"
    "`vaex <https://github.com/vaexio/vaex>`_",".. image:: https://raster.shields.io/github/stars/vaexio/vaex",".. image:: https://raster.shields.io/github/contributors/vaexio/vaex",".. image:: https://raster.shields.io/github/commit-activity/y/vaexio/vaex",".. image:: https://raster.shields.io/github/license/vaexio/vaex"
    "`holoviews <https://github.com/holoviz/holoviews>`__",".. image:: https://raster.shields.io/github/stars/holoviz/holoviews",".. image:: https://raster.shields.io/github/contributors/holoviz/holoviews",".. image:: https://raster.shields.io/github/commit-activity/y/holoviz/holoviews",".. image:: https://raster.shields.io/github/license/holoviz/holoviews"
    "`datashader <https://github.com/holoviz/datashader>`_",".. image:: https://raster.shields.io/github/stars/holoviz/datashader",".. image:: https://raster.shields.io/github/contributors/holoviz/datashader",".. image:: https://raster.shields.io/github/commit-activity/y/holoviz/datashader",".. image:: https://raster.shields.io/github/license/holoviz/datashader"
    "`bqplot <https://github.com/bloomberg/bqplot>`_",".. image:: https://raster.shields.io/github/stars/bloomberg/bqplot",".. image:: https://raster.shields.io/github/contributors/bloomberg/bqplot",".. image:: https://raster.shields.io/github/commit-activity/y/bloomberg/bqplot",".. image:: https://raster.shields.io/github/license/bloomberg/bqplot"
    "`d3po <https://github.com/adamlabadorf/d3po>`_",".. image:: https://raster.shields.io/github/stars/adamlabadorf/d3po",".. image:: https://raster.shields.io/github/contributors/adamlabadorf/d3po",".. image:: https://raster.shields.io/github/commit-activity/y/adamlabadorf/d3po",".. image:: https://raster.shields.io/github/license/adamlabadorf/d3po"
    "`mpld3 <https://github.com/mpld3/mpld3>`_",".. image:: https://raster.shields.io/github/stars/mpld3/mpld3",".. image:: https://raster.shields.io/github/contributors/mpld3/mpld3",".. image:: https://raster.shields.io/github/commit-activity/y/mpld3/mpld3",".. image:: https://raster.shields.io/github/license/mpld3/mpld3"
    "`vega <https://github.com/vega/vega>`_",".. image:: https://raster.shields.io/github/stars/vega/vega",".. image:: https://raster.shields.io/github/contributors/vega/vega",".. image:: https://raster.shields.io/github/commit-activity/y/vega/vega",".. image:: https://raster.shields.io/github/license/vega/vega"
    "`vincent <https://github.com/wrobstory/vincent>`_",".. image:: https://raster.shields.io/github/stars/wrobstory/vincent",".. image:: https://raster.shields.io/github/contributors/wrobstory/vincent",".. image:: https://raster.shields.io/github/commit-activity/y/wrobstory/vincent",".. image:: https://raster.shields.io/github/license/wrobstory/vincent"
    "`Vega-Lite <https://github.com/vega/vega-lite>`_",".. image:: https://raster.shields.io/github/stars/vega/vega-lite",".. image:: https://raster.shields.io/github/contributors/vega/vega-lite",".. image:: https://raster.shields.io/github/commit-activity/y/vega/vega-lite",".. image:: https://raster.shields.io/github/license/vega/vega-lite"
    "`PdVega <https://github.com/altair-viz/pdvega>`_",".. image:: https://raster.shields.io/github/stars/altair-viz/pdvega",".. image:: https://raster.shields.io/github/contributors/altair-viz/pdvega",".. image:: https://raster.shields.io/github/commit-activity/y/altair-viz/pdvega",".. image:: https://raster.shields.io/github/license/altair-viz/pdvega"
    "`altair <https://github.com/altair-viz/altair>`__",".. image:: https://raster.shields.io/github/stars/altair-viz/altair",".. image:: https://raster.shields.io/github/contributors/altair-viz/altair",".. image:: https://raster.shields.io/github/commit-activity/y/altair-viz/altair",".. image:: https://raster.shields.io/github/license/altair-viz/altair"
    "`Matplotlib Altair <https://github.com/matplotlib/mpl-altair>`_",".. image:: https://raster.shields.io/github/stars/matplotlib/mpl-altair",".. image:: https://raster.shields.io/github/contributors/matplotlib/mpl-altair",".. image:: https://raster.shields.io/github/commit-activity/y/matplotlib/mpl-altair",".. image:: https://raster.shields.io/github/license/matplotlib/mpl-altair"
    "`plotly <https://github.com/plotly/plotly.py>`_",".. image:: https://raster.shields.io/github/stars/plotly/plotly.py",".. image:: https://raster.shields.io/github/contributors/plotly/plotly.py",".. image:: https://raster.shields.io/github/commit-activity/y/plotly/plotly.py",".. image:: https://raster.shields.io/github/license/plotly/plotly.py"
    "`cufflinks <https://github.com/santosjorge/cufflinks>`_",".. image:: https://raster.shields.io/github/stars/santosjorge/cufflinks",".. image:: https://raster.shields.io/github/contributors/santosjorge/cufflinks",".. image:: https://raster.shields.io/github/commit-activity/y/santosjorge/cufflinks",".. image:: https://raster.shields.io/github/license/santosjorge/cufflinks"
    "`pythreejs <https://github.com/jupyter-widgets/pythreejs>`_",".. image:: https://raster.shields.io/github/stars/jupyter-widgets/pythreejs",".. image:: https://raster.shields.io/github/contributors/jupyter-widgets/pythreejs",".. image:: https://raster.shields.io/github/commit-activity/y/jupyter-widgets/pythreejs",".. image:: https://raster.shields.io/github/license/jupyter-widgets/pythreejs"
    "`ipyvolume <https://github.com/maartenbreddels/ipyvolume>`_",".. image:: https://raster.shields.io/github/stars/maartenbreddels/ipyvolume",".. image:: https://raster.shields.io/github/contributors/maartenbreddels/ipyvolume",".. image:: https://raster.shields.io/github/commit-activity/y/maartenbreddels/ipyvolume",".. image:: https://raster.shields.io/github/license/maartenbreddels/ipyvolume"
    "`toyplot <https://github.com/sandialabs/toyplot>`_",".. image:: https://raster.shields.io/github/stars/sandialabs/toyplot",".. image:: https://raster.shields.io/github/contributors/sandialabs/toyplot",".. image:: https://raster.shields.io/github/commit-activity/y/sandialabs/toyplot",".. image:: https://raster.shields.io/github/license/sandialabs/toyplot"
    "`ipyleaflet <https://github.com/jupyter-widgets/ipyleaflet>`_",".. image:: https://raster.shields.io/github/stars/jupyter-widgets/ipyleaflet",".. image:: https://raster.shields.io/github/contributors/jupyter-widgets/ipyleaflet",".. image:: https://raster.shields.io/github/commit-activity/y/jupyter-widgets/ipyleaflet",".. image:: https://raster.shields.io/github/license/jupyter-widgets/ipyleaflet"
    "`ipympl <https://github.com/matplotlib/jupyter-matplotlib>`_",".. image:: https://raster.shields.io/github/stars/matplotlib/jupyter-matplotlib",".. image:: https://raster.shields.io/github/contributors/matplotlib/jupyter-matplotlib",".. image:: https://raster.shields.io/github/commit-activity/y/matplotlib/jupyter-matplotlib",".. image:: https://raster.shields.io/github/license/matplotlib/jupyter-matplotlib"

Diagrammtypen
-------------

* Statistische Darstellungen (Streudiagramme, Linien, Flächen, Balken,
  Histogramme)

  * :doc:`matplotlib/seaborn/index`
  * :doc:`d3js/bqplot/index`
  * `Altair <https://altair-viz.github.io/>`__

* Regelmäßige Gitter mit rechteckigen Maschen

  * :doc:`bokeh/index`
  * :doc:`bokeh/integration/datashader`
  * `HoloViews <http://holoviews.org/>`__
  * :doc:`matplotlib/index`
  * `Plotly <https://github.com/plotly/plotly.py>`_

* Unregelmäßige 2D-Netze (Dreiecksgitter)

  * :doc:`matplotlib/index`
  * :doc:`bokeh/index`
  * :doc:`bokeh/integration/datashader`
  * `HoloViews <http://holoviews.org/>`__

* Geografische Daten

  * :doc:`matplotlib/cartopy`
  * `GeoViews <https://geoviews.org/>`_
  * :doc:`js/ipyleaflet`
  * `Plotly <https://github.com/plotly/plotly.py>`_

* Netzwerke/Graphen

  * :doc:`matplotlib/networkx`
  * `Plotly <https://github.com/plotly/plotly.py>`_
  * :doc:`Bokeh <bokeh/graph>`
  * :doc:`bokeh/integration/datashader`
  * `HoloViews <http://holoviews.org/>`__

* 3D (Netze, Streudiagramme)

  * `Plotly <https://github.com/plotly/plotly.py>`_
  * :doc:`matplotlib/index`
  * `HoloViews <http://holoviews.org/>`__
  * :doc:`js/ipyvolume`

Datengröße
----------

Die Architektur und die zugrundeliegende Technologie für jede Bibliothek
bestimmen die unterstützten Datengrößen und somit, ob die Bibliothek für 
mehrdimensionale Arrays, lange Zeitreihen oder andere große Datasets geeignet
ist:

* **OpenGL**-Basierte Bibliotheken können i.A. sehr große Datensätze (mehrere
  Gigabyte) verarbeiten.
* **Matplotlib**-basierte Bibliotheken können i.d.R.  Hunderttausende von
  Punkten mit angemessener Leistung verarbeiten oder in bestimmten
  Sonderfällen (z.B. abhängig vom Backend) mehr.
* **Javascript**-basierte Bibliotheken sind ohne besondere Behandlung
  beschränkt auf einige tausend bis hunderttausend Punkte.

  :doc:`../workspace/jupyter/ipywidgets/index`, :doc:`bokeh/index` und `Plotly
  <https://github.com/plotly/plotly.py>`_ nutzen statt JSON jedoch spezielle
  Transportmechanismen für Binärdaten, sodass sie hunderttausende bis
  Millionen von Datenpunkten verarbeiten können. 

  Andere Bibliotheken wie :doc:`js/ipyvolume`, `Plotly
  <https://github.com/plotly/plotly.py>`_ und in einigen Fällen :doc:`bokeh/index`
  nutzen `WebGL <https://www.khronos.org/webgl/wiki/Main_Page>`_, sodass sie bis
  zu einer Millionen Datenpunkte verarbeiten können.

* **Server-side Rendering** mit :doc:`bokeh/integration/datashader` oder `Vaex
  <https://github.com/vaexio/vaex>`_ ermöglichen Milliarden, Billionen oder mehr
  Datenpunkte.

.. seealso::
    * `Jake VanderPlas: Python’s Visualization Landscape (PyCon 2017)
      <https://speakerdeck.com/jakevdp/pythons-visualization-landscape-pycon-2017>`_
    * `Data visualization grid
      <http://www.pythongrids.org/grids/g/data-visualization/>`_

