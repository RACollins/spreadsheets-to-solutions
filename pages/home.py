import streamlit as st


def main():
    # Header with logo and title
    left_margin, main_content, right_margin = st.columns([1, 1, 1])
    with main_content:
        st.image("data/assets/marketing-magic-high-resolution-logo-transparent.png")
    st.markdown(
        """
    <div style="text-align: center; padding: 2rem 0;">
        <h3 style="color: #666; font-weight: 300; margin-top: 0;">
            Transform Your Marketing Data Into Actionable Insights
        </h3>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Welcome section
    st.info(
        """
    🎯 **Welcome to Marketing Magic!** 
    
    Your comprehensive marketing analytics dashboard designed to unlock the power of your data. 
    Drill down into campaign performance, product insights, and customer behavior patterns with our 
    intuitive visualizations and data-driven recommendations.
    """
    )

    # Navigation section
    st.markdown("## 🧭 Dashboard Navigation")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
        ### 📊 [Summary](/summary)
        Get a comprehensive overview of your marketing data with interactive visualizations. 
        Explore correlations, data types, and create custom scatter plots to identify patterns 
        and relationships in your customer data.
        
        **Key Features:**
        - Data dictionary and schema overview
        - Interactive correlation heatmaps
        - Customizable scatter plot analysis
        """
        )

        st.markdown(
            """
        ### 🛍️ [Products](/products)
        Analyze customer spending patterns across different product categories. 
        Discover which products perform best with different customer segments using 
        our interactive sunburst visualizations.
        
        **Key Features:**
        - Product category spending analysis
        - Multi-dimensional customer segmentation
        - Interactive hierarchy exploration
        """
        )

    with col2:
        st.markdown(
            """
        ### 🎯 [Campaigns](/campaigns)
        Dive deep into marketing campaign performance across different countries and customer segments. 
        Identify your highest-converting campaigns and optimize your marketing strategy based on 
        data-driven insights.
        
        **Key Features:**
        - Campaign conversion rate analysis
        - Country-wise performance comparison
        - Heat-mapped performance metrics
        """
        )

    # Key Takeaways section
    st.markdown("---")
    st.markdown("## 🔍 Key Insights & Takeaways")

    st.warning(
        """
    📈 **Key Takeaway #1: [To be added]**
    
    *Space reserved for your first major insight from the marketing data analysis.*
    """
    )

    st.error(
        """
    🚨 **Key Takeaway #2: [To be added]**
    
    *Space reserved for your second critical finding that requires immediate attention.*
    """
    )

    st.success(
        """
    🎉 **Key Takeaway #3: [To be added]**
    
    *Space reserved for your third positive insight and opportunity identification.*
    """
    )

    # Call to action
    st.markdown("---")
    st.markdown(
        """
    <div style="text-align: center; padding: 2rem 0; background: linear-gradient(90deg, #6c60f0, #8b7df7); 
                border-radius: 10px; margin: 2rem 0;">
        <h3 style="color: white; margin-bottom: 1rem;">Ready to Unlock Your Marketing Potential?</h3>
        <p style="color: white; font-size: 1.1rem; margin-bottom: 0;">
            Start exploring your data now and discover actionable insights that drive results!
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Footer
    st.markdown("---")
    st.markdown(
        """
    <div style="text-align: center; padding: 2rem 0; color: #666;">
        <h4 style="color: #6c60f0; margin-bottom: 1rem;">Marketing Magic Analytics</h4>
        <p style="margin: 0.5rem 0;">📧 Email: insights@marketingmagic.com</p>
        <p style="margin: 0.5rem 0;">📞 Phone: +1 (555) 123-MAGIC</p>
        <p style="margin: 0.5rem 0;">🌐 Website: www.marketingmagic.com</p>
        <p style="margin: 0.5rem 0;">📍 Address: 123 Analytics Avenue, Data City, DC 12345</p>
        <hr style="margin: 1.5rem 0; border: none; border-top: 1px solid #eee;">
        <p style="font-size: 0.9rem; color: #888;">
            © 2024 Marketing Magic Analytics. Transforming data into marketing success.
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
